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

    def validate_critical_data(self):
        """Check for missing critical data required for the character to function."""
        # Validate S.P.E.C.I.A.L. attributes - all 7 must be present and valid
        attrs = self.character.get_special_attributes()
        required_attrs = ['Strength', 'Perception', 'Endurance', 'Charisma', 'Intelligence', 'Agility', 'Luck']
        for attr_name in required_attrs:
            if attr_name not in attrs:
                self.health_warnings.append(f"Missing attribute: {attr_name}")
            elif attrs[attr_name] < 1:
                self.health_warnings.append(f"{attr_name} is below 1: {attrs[attr_name]}")

        # Validate level exists and is valid
        if self.character.level < 1:
            self.health_warnings.append(f"Level is invalid: {self.character.level} (expected >= 1)")

        # Validate derived stats can be calculated
        derived_stats = self.character.derived_stats
        if derived_stats['max_health'] == 0:
            self.health_warnings.append("Max health is 0 (calculation error)")

        # Validate skills exist (required for character type)
        if self.character.type == 'character':
            skills = self.character.get_skills()
            if not skills:
                self.health_warnings.append("No skills found (required for character)")
            elif len(skills) < 17:
                self.health_warnings.append(f"Missing skills: only {len(skills)} of 17 found")

    def validate_completeness(self):
        """Check for optional but recommended fields (info only, not errors)."""
        if not self.character.get_origin():
            self.completeness_issues.append("Origin is empty")

        if not self.character.get_biography():
            self.completeness_issues.append("Biography is empty (DATA tab)")

        # Check for tagged skills
        skills = self.character.get_skills()
        tagged_skills = [s for s in skills if s.get('tag', False)]
        if self.character.type == 'character' and len(tagged_skills) == 0:
            self.completeness_issues.append("No tagged skills")

        # Check perks
        perks = self.character.get_perks()
        if not perks:
            self.completeness_issues.append("No perks")

        # Check equipped weapons (not stashed = equipped)
        weapons = self.character.get_weapons()
        equipped_weapons = [w for w in weapons if not w.get('system', {}).get('stashed', False)]
        if weapons and not equipped_weapons:
            self.completeness_issues.append(f"No weapons equipped ({len(weapons)} available)")

        # Check equipped apparel (not stashed = equipped)
        if self.character.type != 'robot':
            apparel = self.character.get_apparel()
            equipped_apparel = [a for a in apparel if not a.get('system', {}).get('stashed', False)]
            if apparel and not equipped_apparel:
                self.completeness_issues.append(f"No apparel equipped ({len(apparel)} available)")

        # Check for missing descriptions in important items
        for item in self.character.get_items():
            item_type = item.get('type')
            # Only check perks and traits - they should have descriptions
            if item_type in ['perk', 'trait']:
                description = self.character.strip_html(item.get('system', {}).get('description', ''))
                if not description:
                    self.completeness_issues.append(f"Missing description: {item.get('name', 'unknown')} ({item_type})")

    def run_validation(self, verbose: bool = True):
        """Run all validation checks."""
        if verbose:
            print(f"Running validation for: {self.character.name}")
        self.validate_critical_data()
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
        print("## Summary")
        print("-" * 70)
        if len(self.health_warnings) == 0 and len(self.completeness_issues) == 0:
            print("[OK] Validation PASSED - No issues found")
        elif len(self.health_warnings) == 0:
            print(f"[OK] Validation PASSED - {len(self.completeness_issues)} info item(s)")
        else:
            print(f"[!] Validation found {len(self.health_warnings)} warning(s)")
        print(f"\n{'='*70}\n")

        # Return True (success) if no health warnings - completeness issues are just info
        return len(self.health_warnings) == 0

def main():
    parser = argparse.ArgumentParser(
        description="Validate FVTT Fallout character JSON exports.",
        epilog="Example:\n  python -m lib.fallout_validator fvtt_export/character.json"
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
