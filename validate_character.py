#!/usr/bin/env python3
"""
Fallout Character Data Validation Tool (Refactored)

Validates FVTT Fallout character JSON exports using the shared character library.
It checks for schema structure, data health, and completeness.
"""

import sys
import json
import argparse
from pathlib import Path

# Import the shared library components
from lib.character_data import Character
from lib.safe_path import validate_path


class CharacterValidator:
    """Validates a Character object for quality and completeness."""

    def __init__(self, character: Character):
        """Initializes the validator with a Character object."""
        self.character = character
        self.health_warnings = []
        self.completeness_issues = []

    def validate_health_checks(self):
        """Check for unusual or invalid values using data from the Character object."""
        # Validate S.P.E.C.I.A.L. attributes
        attrs = self.character.get_special_attributes()
        for attr_name, value in attrs.items():
            if value < 1:
                self.health_warnings.append(f"{attr_name} is below 1: {value}")
            elif value > 15:
                self.health_warnings.append(f"{attr_name} is unusually high: {value} (expected 1-10)")

        # Validate level
        if self.character.level < 1:
            self.health_warnings.append(f"Level is invalid: {self.character.level} (expected >= 1)")
        elif self.character.level > 50:
            self.health_warnings.append(f"Level is unusually high: {self.character.level}")

        # Validate health
        derived_stats = self.character.derived_stats
        if derived_stats['current_health'] < 0:
            self.health_warnings.append(f"Health is negative: {derived_stats['current_health']}")
        if derived_stats['max_health'] == 0:
            self.health_warnings.append("Max health is 0 (calculated value should be higher)")
        if derived_stats['current_health'] > derived_stats['max_health'] > 0:
            self.health_warnings.append(f"Health {derived_stats['current_health']} exceeds max {derived_stats['max_health']}")

        # Validate radiation
        if derived_stats['radiation'] < 0:
            self.health_warnings.append(f"Radiation is negative: {derived_stats['radiation']}")
        elif derived_stats['radiation'] > 0:
            self.health_warnings.append(f"Radiation level: {derived_stats['radiation']} (reduces max health)")

        # Validate body parts status
        for part in self.character.get_body_parts():
            status = part['status'].lower()
            if status not in ['healthy', 'injured', 'crippled']:
                self.health_warnings.append(f"{part['name']}: unusual status '{part['status']}'")
            elif status == 'crippled':
                self.health_warnings.append(f"{part['name']}: CRIPPLED")
            elif status == 'injured':
                self.health_warnings.append(f"{part['name']}: injured")

            if part['injuries_open'] > 0:
                self.health_warnings.append(f"{part['name']}: {part['injuries_open']} untreated injury(s)")
            if part['injuries_treated'] > 0:
                self.health_warnings.append(f"{part['name']}: {part['injuries_treated']} treated injury(s)")

        # Check for items with negative quantities
        for item in self.character.get_items():
            quantity = item.get('system', {}).get('quantity', 0)
            if quantity < 0:
                self.health_warnings.append(f"Negative quantity: {item.get('name', 'unknown')} ({quantity})")

    def validate_completeness(self):
        """Check for missing or empty fields."""
        if not self.character.get_origin():
            self.completeness_issues.append("Origin is empty")

        if not self.character.get_biography():
            self.completeness_issues.append("Biography is empty (DATA tab)")

        # Check skill count
        skills = self.character.get_skills()
        if self.character.type == 'character':
            if not skills:
                self.completeness_issues.append("No skills found")
            elif len(skills) < 17:
                self.completeness_issues.append(f"Only {len(skills)} skills (expected 17)")

        # Check for tagged skills
        tagged_skills = [s for s in skills if s.get('tag', False)]
        if self.character.type == 'character' and len(tagged_skills) == 0:
            self.completeness_issues.append("No tagged skills")
        elif tagged_skills:
            tag_names = [s['name'] for s in tagged_skills]
            self.completeness_issues.append(f"Tagged skills ({len(tagged_skills)}): {', '.join(tag_names)}")

        # Check perks
        perks = self.character.get_perks()
        if perks:
            perk_names = [p['name'] for p in perks]
            self.completeness_issues.append(f"Perks ({len(perks)}): {', '.join(perk_names)}")
        else:
            self.completeness_issues.append("No perks")

        # Check equipped weapons
        weapons = self.character.get_weapons()
        equipped_weapons = [w for w in weapons if w.get('equipped', False)]
        if weapons and not equipped_weapons:
            weapon_names = [w['name'] for w in weapons]
            self.completeness_issues.append(f"No weapons equipped (available: {', '.join(weapon_names)})")
        elif equipped_weapons:
            weapon_names = [w['name'] for w in equipped_weapons]
            self.completeness_issues.append(f"Equipped weapons: {', '.join(weapon_names)}")

        # Check equipped apparel
        if self.character.type != 'robot':
            apparel = self.character.get_apparel()
            equipped_apparel = [a for a in apparel if a.get('equipped', False)]
            if apparel and not equipped_apparel:
                apparel_names = [a['name'] for a in apparel]
                self.completeness_issues.append(f"No apparel equipped (available: {', '.join(apparel_names)})")
            elif equipped_apparel:
                apparel_names = [a['name'] for a in equipped_apparel]
                self.completeness_issues.append(f"Equipped apparel: {', '.join(apparel_names)}")

        # Check for missing descriptions in items that should have them
        items_missing_description = []
        for item in self.character.get_items():
            item_type = item.get('type')
            if item_type not in ['skill', 'ammo']: # Types that often have no description
                description = self.character.strip_html(item.get('system', {}).get('description', ''))
                if not description:
                    items_missing_description.append(f"{item.get('name', 'unknown')} ({item_type})")

        if items_missing_description:
            for item_info in items_missing_description:
                self.completeness_issues.append(f"Missing description: {item_info}")

    def run_validation(self):
        """Run all validation checks."""
        print(f"Running validation for: {self.character.name}")
        self.validate_health_checks()
        self.validate_completeness()

    def print_report(self) -> bool:
        """Prints the validation report and returns True if no issues were found."""
        print(f"\n{'='*70}")
        print(f"Character Validation Report: {self.character.name}")
        print(f"{'='*70}")
        print(f"File: {self.character.character_file.name}")
        print(f"Type: {self.character.type}")
        print(f"{'='*70}\n")

        # Health Checks
        print("## Health Checks")
        print("-" * 70)
        if self.health_warnings:
            print(f"[!] Found {len(self.health_warnings)} warning(s):\n")
            for idx, warning in enumerate(self.health_warnings, 1):
                print(f"  {idx}. {warning}")
        else:
            print("[OK] All health checks passed - no unusual values detected")
        print()

        # Completeness Report
        print("## Completeness Report")
        print("-" * 70)
        if self.completeness_issues:
            print(f"[i] Found {len(self.completeness_issues)} item(s):\n")
            for idx, issue in enumerate(self.completeness_issues, 1):
                print(f"  {idx}. {issue}")
        else:
            print("[OK] Character data is complete - all expected fields populated")
        print()

        # Summary
        total_issues = len(self.health_warnings) + len(self.completeness_issues)
        print("## Summary")
        print("-" * 70)
        if total_issues == 0:
            print("[OK] Validation PASSED - Character data is valid and complete")
        else:
            print(f"[i] Validation completed:")
            print(f"   - Health warnings: {len(self.health_warnings)}")
            print(f"   - Info items: {len(self.completeness_issues)}")
        print(f"\n{'='*70}\n")

        return total_issues == 0

def main():
    parser = argparse.ArgumentParser(
        description="Validate FVTT Fallout character JSON exports.",
        epilog="Example:\n  python validate_character.py fvtt_export/character.json"
    )
    parser.add_argument('character_file', type=Path, help='Path to FVTT character JSON file')
    args = parser.parse_args()

    try:
        # Security: Validate the path before using it
        safe_file_path = validate_path(args.character_file, base_dir='fvtt_export')

        # Load character using the central library
        character = Character(safe_file_path)

        # Run validation
        validator = CharacterValidator(character)
        validator.run_validation()
        success = validator.print_report()

        # Exit with status 0 for success, 1 for issues found
        sys.exit(0 if success else 1)

    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
