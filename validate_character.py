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
                self.health_warnings.append(f"S.P.E.C.I.A.L. {attr_name.upper()} is below 1: {value}")
            elif value > 15:
                self.health_warnings.append(f"S.P.E.C.I.A.L. {attr_name.upper()} is unusually high: {value} (expected 1-10 range)")

        # Validate level
        if self.character.level < 1:
            self.health_warnings.append(f"Character level is invalid: {self.character.level} (expected >= 1)")
        elif self.character.level > 50:
            self.health_warnings.append(f"Character level is unusually high: {self.character.level}")

        # Validate health
        derived_stats = self.character.derived_stats
        if derived_stats['current_health'] < 0:
            self.health_warnings.append(f"Current health is negative: {derived_stats['current_health']}")
        if derived_stats['max_health'] == 0:
            self.health_warnings.append("Max health is 0 (likely needs calculation)")
        if derived_stats['current_health'] > derived_stats['max_health'] > 0:
            self.health_warnings.append(f"Current health ({derived_stats['current_health']}) exceeds max health ({derived_stats['max_health']})")

        # Validate radiation
        if derived_stats['radiation'] < 0:
            self.health_warnings.append(f"Radiation is negative: {derived_stats['radiation']}")

        # Validate body parts status
        for part in self.character.get_body_parts():
            if part['status'].lower() not in ['healthy', 'injured', 'crippled']:
                self.health_warnings.append(f"Body part '{part['name']}' has unusual status: '{part['status']}'")
            if part['injuries_open'] > 0:
                self.health_warnings.append(f"Body part '{part['name']}' has {part['injuries_open']} untreated injury/injuries")

        # Check for items with negative quantities
        all_items = self.character.get_items()
        for item in all_items:
            if 'quantity' in item.get('system', {}) and item['system']['quantity'] < 0:
                self.health_warnings.append(f"Item '{item.get('name', 'unknown')}' has negative quantity: {item['system']['quantity']}")

    def validate_completeness(self):
        """Check for missing or empty fields."""
        if not self.character.get_origin():
            self.completeness_issues.append("Character origin is empty")

        if not self.character.get_biography():
            self.completeness_issues.append("Character biography is empty (no background data)")

        # Check skill count
        skills = self.character.get_skills()
        if self.character.type == 'character':
            if not skills:
                self.completeness_issues.append("Character has no skills")
            elif len(skills) < 17:
                self.completeness_issues.append(f"Character has only {len(skills)} skills (expected 17)")

        # Check for missing descriptions in items that should have them
        items_missing_description = []
        for item in self.character.get_items():
            item_type = item.get('type')
            if item_type not in ['skill', 'ammo']: # Types that often have no description
                description = self.character.strip_html(item.get('system', {}).get('description', ''))
                if not description:
                    items_missing_description.append(f"{item.get('name', 'unknown')} ({item_type})")

        if items_missing_description:
            self.completeness_issues.append(f"{len(items_missing_description)} items are missing descriptions")

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
            print(f"⚠️  Found {len(self.health_warnings)} warning(s):\n")
            for idx, warning in enumerate(self.health_warnings, 1):
                print(f"  {idx}. {warning}")
        else:
            print("✅ All health checks passed - no unusual values detected")
        print()

        # Completeness Report
        print("## Completeness Report")
        print("-" * 70)
        if self.completeness_issues:
            print(f"ℹ️  Found {len(self.completeness_issues)} completeness issue(s):\n")
            for idx, issue in enumerate(self.completeness_issues, 1):
                print(f"  {idx}. {issue}")
        else:
            print("✅ Character data is complete - all expected fields populated")
        print()

        # Summary
        total_issues = len(self.health_warnings) + len(self.completeness_issues)
        print("## Summary")
        print("-" * 70)
        if total_issues == 0:
            print("✅ Validation PASSED - Character data is valid and complete")
        else:
            print(f"⚠️  Validation completed with {total_issues} total issue(s):")
            print(f"   - Health warnings: {len(self.health_warnings)}")
            print(f"   - Completeness issues: {len(self.completeness_issues)}")
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
