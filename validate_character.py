#!/usr/bin/env python3
"""
Fallout Character Data Validation Tool

Validates FVTT Fallout character JSON exports for:
- Schema structure (required fields present)
- Health checks (unusual/invalid values)
- Completeness report (missing/empty fields)

Usage:
    python validate_character.py <character_json_file>
    python validate_character.py --all  # Validate all characters in fvtt_export/
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple
from datetime import datetime


class CharacterValidator:
    """Validates FVTT Fallout character JSON exports for quality and completeness."""

    def __init__(self, character_file: Path):
        self.character_file = character_file
        self.character_data = None
        self.character_name = None
        self.character_type = None

        # Validation results
        self.schema_errors = []
        self.health_warnings = []
        self.completeness_issues = []

    def load_character(self) -> bool:
        """Load character JSON file."""
        try:
            with open(self.character_file, 'r', encoding='utf-8') as f:
                self.character_data = json.load(f)

            self.character_name = self.character_data.get('name', 'Unknown')
            self.character_type = self.character_data.get('type', 'Unknown')

            return True
        except json.JSONDecodeError as e:
            self.schema_errors.append(f"Invalid JSON format: {e}")
            return False
        except Exception as e:
            self.schema_errors.append(f"Failed to load file: {e}")
            return False

    def validate_schema(self):
        """Validate JSON schema structure against expected FVTT format."""

        # Top-level required fields
        required_top_level = ['_stats', 'name', 'type', 'system', 'items']
        for field in required_top_level:
            if field not in self.character_data:
                self.schema_errors.append(f"Missing top-level field: '{field}'")

        # Validate _stats metadata
        if '_stats' in self.character_data:
            stats = self.character_data['_stats']
            required_stats = ['systemId', 'systemVersion', 'coreVersion']
            for field in required_stats:
                if field not in stats:
                    self.schema_errors.append(f"Missing _stats field: '{field}'")

            # Check system ID
            if stats.get('systemId') != 'fallout':
                self.schema_errors.append(f"Invalid systemId: '{stats.get('systemId')}' (expected 'fallout')")

        # Validate character type
        valid_types = ['character', 'robot', 'creature', 'npc']
        if self.character_type not in valid_types:
            self.schema_errors.append(f"Invalid character type: '{self.character_type}' (expected one of {valid_types})")

        # Validate system structure
        if 'system' in self.character_data:
            system = self.character_data['system']

            # Required system fields for character types
            if self.character_type == 'character':
                required_system = ['attributes', 'level', 'health', 'defense', 'initiative']
                for field in required_system:
                    if field not in system:
                        self.schema_errors.append(f"Missing system field: '{field}'")

                # Validate attributes structure
                if 'attributes' in system:
                    required_attrs = ['str', 'per', 'end', 'cha', 'int', 'agi', 'luc']
                    attrs = system['attributes']
                    for attr in required_attrs:
                        if attr not in attrs:
                            self.schema_errors.append(f"Missing S.P.E.C.I.A.L. attribute: '{attr}'")
                        elif not isinstance(attrs.get(attr), dict) or 'value' not in attrs.get(attr, {}):
                            self.schema_errors.append(f"Invalid attribute structure for '{attr}' (missing 'value')")

                # Validate body_parts structure
                if 'body_parts' in system:
                    required_parts = ['head', 'torso', 'armL', 'armR', 'legL', 'legR']
                    body_parts = system['body_parts']
                    for part in required_parts:
                        if part not in body_parts:
                            self.schema_errors.append(f"Missing body part: '{part}'")
                        else:
                            part_data = body_parts[part]
                            if 'status' not in part_data:
                                self.schema_errors.append(f"Body part '{part}' missing 'status' field")
                            if 'resistance' not in part_data:
                                self.schema_errors.append(f"Body part '{part}' missing 'resistance' field")

        # Validate items array
        if 'items' not in self.character_data:
            self.schema_errors.append("Missing 'items' array")
        elif not isinstance(self.character_data['items'], list):
            self.schema_errors.append("'items' field is not an array")
        else:
            # Check item structure
            for idx, item in enumerate(self.character_data['items']):
                if not isinstance(item, dict):
                    self.schema_errors.append(f"Item {idx} is not an object")
                    continue

                if 'type' not in item:
                    self.schema_errors.append(f"Item {idx} missing 'type' field")
                if 'name' not in item:
                    self.schema_errors.append(f"Item {idx} missing 'name' field")
                if 'system' not in item:
                    self.schema_errors.append(f"Item {idx} ({item.get('name', 'unknown')}) missing 'system' field")

    def validate_health_checks(self):
        """Check for unusual or invalid values."""

        if 'system' not in self.character_data:
            return

        system = self.character_data['system']

        # Validate S.P.E.C.I.A.L. attributes (should be 1-10+)
        if 'attributes' in system:
            attrs = system['attributes']
            for attr_name in ['str', 'per', 'end', 'cha', 'int', 'agi', 'luc']:
                if attr_name in attrs:
                    value = attrs[attr_name].get('value', 0)
                    if value < 1:
                        self.health_warnings.append(f"S.P.E.C.I.A.L. {attr_name.upper()} is below 1: {value}")
                    elif value > 15:
                        self.health_warnings.append(f"S.P.E.C.I.A.L. {attr_name.upper()} is unusually high: {value} (expected 1-10 range)")

        # Validate level (should be 1+)
        if 'level' in system:
            level = system['level'].get('value', 0)
            if level < 1:
                self.health_warnings.append(f"Character level is invalid: {level} (expected >= 1)")
            elif level > 50:
                self.health_warnings.append(f"Character level is unusually high: {level}")

        # Validate health
        if 'health' in system:
            health = system['health']
            current = health.get('value', 0)
            max_health = health.get('max', 0)

            if current < 0:
                self.health_warnings.append(f"Current health is negative: {current}")

            if max_health == 0:
                self.health_warnings.append("Max health is 0 (likely needs calculation)")

            if max_health > 0 and current > max_health:
                self.health_warnings.append(f"Current health ({current}) exceeds max health ({max_health})")

        # Validate radiation (should be 0-10+)
        radiation = system.get('radiation', 0)
        if radiation < 0:
            self.health_warnings.append(f"Radiation is negative: {radiation}")
        elif radiation > 10:
            self.health_warnings.append(f"Radiation is very high: {radiation} (character may be heavily irradiated)")

        # Validate conditions (should be 0-5 typically)
        if 'conditions' in system:
            conditions = system['conditions']
            condition_names = ['hunger', 'thirst', 'sleep', 'fatigue', 'intoxication']
            for cond in condition_names:
                if cond in conditions:
                    value = conditions[cond]
                    if value < 0:
                        self.health_warnings.append(f"Condition '{cond}' is negative: {value}")
                    elif value > 5:
                        self.health_warnings.append(f"Condition '{cond}' is very high: {value} (may need attention)")

        # Validate body parts status
        if 'body_parts' in system:
            body_parts = system['body_parts']
            for part_name, part_data in body_parts.items():
                status = part_data.get('status', 'healthy')
                if status not in ['healthy', 'injured', 'crippled']:
                    self.health_warnings.append(f"Body part '{part_name}' has unusual status: '{status}'")

                # Check for untreated injuries
                open_injuries = part_data.get('injuryOpenCount', 0)
                if open_injuries > 0:
                    self.health_warnings.append(f"Body part '{part_name}' has {open_injuries} untreated injury/injuries")

                # Check resistance values (typically 0-10)
                resistance = part_data.get('resistance', {})
                for res_type, res_value in resistance.items():
                    if res_value < 0:
                        self.health_warnings.append(f"Body part '{part_name}' has negative {res_type} resistance: {res_value}")

        # Validate derived stats exist (defense, initiative should be calculated)
        if 'defense' in system:
            defense = system['defense'].get('value', 0)
            if defense == 0:
                # Check if bonus exists
                bonus = system['defense'].get('bonus', 0)
                attrs = system.get('attributes', {})
                agi = attrs.get('agi', {}).get('value', 0)
                if agi >= 9 and bonus == 0:
                    self.health_warnings.append("Defense value is 0 but should be calculated (AGI >= 9 gives defense 2)")

        if 'initiative' in system:
            initiative = system['initiative'].get('value', 0)
            if initiative == 0:
                self.health_warnings.append("Initiative value is 0 but should be calculated (PER + AGI)")

        # Validate carry weight
        if 'carryWeight' in system:
            carry = system['carryWeight']
            current = carry.get('value', 0)

            if current < 0:
                self.health_warnings.append(f"Carry weight is negative: {current}")

        # Check items for issues
        items = self.character_data.get('items', [])

        # Count skills - characters should have skills
        skills = [item for item in items if item.get('type') == 'skill']
        if self.character_type == 'character' and len(skills) == 0:
            self.health_warnings.append("Character has no skills (unusual for character type)")

        # Check for items with negative quantities
        for item in items:
            if 'system' in item and 'quantity' in item['system']:
                qty = item['system']['quantity']
                if qty < 0:
                    self.health_warnings.append(f"Item '{item.get('name', 'unknown')}' has negative quantity: {qty}")

        # Check for weapons with invalid damage
        weapons = [item for item in items if item.get('type') == 'weapon']
        for weapon in weapons:
            damage = weapon.get('system', {}).get('damage', {}).get('rating', 0)
            if damage < 0:
                self.health_warnings.append(f"Weapon '{weapon.get('name', 'unknown')}' has negative damage: {damage}")

    def validate_completeness(self):
        """Check for missing or empty fields that may affect character sheet generation."""

        if 'system' not in self.character_data:
            return

        system = self.character_data['system']

        # Check for missing origin
        origin = system.get('origin', '')
        if not origin or origin.strip() == '':
            self.completeness_issues.append("Character origin is empty")

        # Check for missing biography
        biography = system.get('biography', '')
        if not biography or biography.strip() == '':
            self.completeness_issues.append("Character biography is empty (no background data)")

        # Check XP tracking
        if 'level' in system:
            level_data = system['level']
            current_xp = level_data.get('currentXP', 0)
            next_level_xp = level_data.get('nextLevelXP', 0)

            if next_level_xp == 0:
                self.completeness_issues.append("Next level XP is 0 (needs calculation)")

        # Check items
        items = self.character_data.get('items', [])

        # Count different item types
        item_types = {}
        items_missing_description = []

        for item in items:
            item_type = item.get('type', 'unknown')
            item_types[item_type] = item_types.get(item_type, 0) + 1

            # Check for missing descriptions
            description = item.get('system', {}).get('description', '')
            if not description or description.strip() == '':
                # Some item types are OK without descriptions
                if item_type not in ['skill']:  # Skills get descriptions from core rules
                    items_missing_description.append(f"{item.get('name', 'unknown')} ({item_type})")

        # Report item type counts
        if self.character_type == 'character':
            # Expected item types for characters
            if 'skill' not in item_types:
                self.completeness_issues.append("Character has no skills")
            elif item_types['skill'] < 17:  # Fallout 2d20 has 17 skills
                self.completeness_issues.append(f"Character has only {item_types['skill']} skills (expected 17)")

            if 'perk' not in item_types:
                self.completeness_issues.append("Character has no perks (unusual for leveled character)")

            if 'weapon' not in item_types:
                self.completeness_issues.append("Character has no weapons")

            if 'apparel' not in item_types:
                self.completeness_issues.append("Character has no apparel/armor")

        # Report items missing descriptions
        if items_missing_description:
            if len(items_missing_description) <= 5:
                self.completeness_issues.append(f"Items missing descriptions: {', '.join(items_missing_description)}")
            else:
                self.completeness_issues.append(f"{len(items_missing_description)} items missing descriptions")

        # Check for empty body parts data
        if 'body_parts' in system:
            body_parts = system['body_parts']
            if not body_parts:
                self.completeness_issues.append("Body parts data is empty")

        # Check for missing conditions tracking
        if 'conditions' not in system:
            self.completeness_issues.append("Conditions tracking is missing")

        # Check for empty resistance data
        if 'resistance' in system:
            resistance = system['resistance']
            if all(v == 0 for v in resistance.values()):
                # This is OK, just note it
                pass  # Not an issue, many characters have 0 resistance

        # Check apparel coverage
        apparel_items = [item for item in items if item.get('type') == 'apparel']
        equipped_apparel = [item for item in apparel_items if item.get('system', {}).get('equipped', False)]

        if not equipped_apparel and apparel_items:
            self.completeness_issues.append(f"Character has {len(apparel_items)} apparel items but none equipped")

        # Check weapons equipped
        weapons = [item for item in items if item.get('type') == 'weapon']
        equipped_weapons = [item for item in weapons if item.get('system', {}).get('equipped', False)]

        if not equipped_weapons and weapons:
            self.completeness_issues.append(f"Character has {len(weapons)} weapons but none equipped")

    def run_validation(self) -> bool:
        """Run all validation checks."""
        if not self.load_character():
            return False

        self.validate_schema()
        self.validate_health_checks()
        self.validate_completeness()

        return True

    def print_report(self):
        """Print validation report."""
        print(f"\n{'='*70}")
        print(f"Character Validation Report: {self.character_name}")
        print(f"{'='*70}")
        print(f"File: {self.character_file.name}")
        print(f"Type: {self.character_type}")
        print(f"{'='*70}\n")

        # Schema Validation
        print("## Schema Validation")
        print("-" * 70)
        if self.schema_errors:
            print(f"❌ Found {len(self.schema_errors)} schema error(s):\n")
            for idx, error in enumerate(self.schema_errors, 1):
                print(f"  {idx}. {error}")
        else:
            print("✅ Schema validation passed - all required fields present")
        print()

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
        print("## Summary")
        print("-" * 70)
        total_issues = len(self.schema_errors) + len(self.health_warnings) + len(self.completeness_issues)

        if total_issues == 0:
            print("✅ Validation PASSED - Character data is valid and complete")
        else:
            print(f"⚠️  Validation completed with {total_issues} total issue(s):")
            print(f"   - Schema errors: {len(self.schema_errors)}")
            print(f"   - Health warnings: {len(self.health_warnings)}")
            print(f"   - Completeness issues: {len(self.completeness_issues)}")

        print(f"\n{'='*70}\n")

        return total_issues == 0


def validate_all_characters(export_dir: Path):
    """Validate all character files in the export directory."""
    character_files = sorted(export_dir.glob('fvtt-Actor-*.json'))

    if not character_files:
        print(f"No character files found in {export_dir}")
        return

    print(f"\n{'='*70}")
    print(f"Validating {len(character_files)} character file(s)")
    print(f"{'='*70}\n")

    results = []

    for char_file in character_files:
        validator = CharacterValidator(char_file)
        validator.run_validation()
        validator.print_report()

        total_issues = len(validator.schema_errors) + len(validator.health_warnings) + len(validator.completeness_issues)
        results.append((char_file.name, validator.character_name, total_issues))

    # Print summary table
    print(f"\n{'='*70}")
    print("Validation Summary")
    print(f"{'='*70}\n")
    print(f"{'Character':<30} {'File':<30} {'Issues':>8}")
    print("-" * 70)

    for filename, char_name, issues in results:
        status = "✅" if issues == 0 else "⚠️ "
        # Truncate long names
        display_name = char_name[:28] + ".." if len(char_name) > 30 else char_name
        display_file = filename[:28] + ".." if len(filename) > 30 else filename
        print(f"{status} {display_name:<28} {display_file:<28} {issues:>6}")

    print(f"\n{'='*70}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_character.py <character_json_file>")
        print("       python validate_character.py --all  # Validate all characters")
        print("\nExample:")
        print("  python validate_character.py fvtt_export/fvtt-Actor-marcel-O44zYNGmMfYtSjVw.json")
        print("  python validate_character.py --all")
        sys.exit(1)

    if sys.argv[1] == '--all':
        export_dir = Path('fvtt_export')
        if not export_dir.exists():
            print(f"Error: Directory not found: {export_dir}")
            sys.exit(1)

        validate_all_characters(export_dir)
    else:
        character_file = Path(sys.argv[1])

        if not character_file.exists():
            print(f"Error: File not found: {character_file}")
            sys.exit(1)

        validator = CharacterValidator(character_file)
        validator.run_validation()
        success = validator.print_report()

        sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
