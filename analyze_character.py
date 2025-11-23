#!/usr/bin/env python3
"""
Fallout Character JSON Analyzer

Recursively extracts ALL fields from FVTT Fallout character JSON exports.
Generates both machine-readable JSON and human-readable Markdown inventory.

Usage:
    python analyze_character.py <character_json_file>
    python analyze_character.py fvtt_export/fvtt-Actor-dr.-eloise-'ellie'-harper-jkTOphZz7Tvl7Qqn.json
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Set, Union
from collections import defaultdict
from datetime import datetime


class CharacterAnalyzer:
    """Analyzes Fallout FVTT character JSON structure comprehensively."""

    def __init__(self, character_file: Path):
        self.character_file = character_file
        self.character_data = None
        self.character_name = None
        self.character_type = None
        self.character_level = None

        # Field tracking
        self.all_fields: Dict[str, Dict[str, Any]] = {}
        self.item_types: Dict[str, Dict] = defaultdict(lambda: {
            'count': 0,
            'fields': {},
            'examples': []
        })

        # Statistics
        self.total_fields = 0
        self.total_items = 0

        # Calculated derived statistics
        self.calculated_stats = {}
        self.formulas = None

    def load_character(self):
        """Load character JSON file."""
        print(f"Loading character from: {self.character_file}")
        with open(self.character_file, 'r', encoding='utf-8') as f:
            self.character_data = json.load(f)

        self.character_name = self.character_data.get('name', 'Unknown')
        self.character_type = self.character_data.get('type', 'Unknown')
        self.character_level = self.character_data.get('system', {}).get('level', {}).get('value', '?')

        print(f"[OK] Loaded: {self.character_name} (Type: {self.character_type}, Level: {self.character_level})")

    def extract_fields_recursive(self, obj: Any, path: str = "", parent_type: str = None):
        """
        Recursively extract all fields from nested JSON structure.

        Args:
            obj: Current object/value being analyzed
            path: JSON path to current location (dot notation)
            parent_type: Type hint for categorization
        """
        if obj is None:
            self._record_field(path, 'null', None, parent_type)
            return

        if isinstance(obj, dict):
            for key, value in obj.items():
                new_path = f"{path}.{key}" if path else key
                self.extract_fields_recursive(value, new_path, parent_type)

        elif isinstance(obj, list):
            if not obj:  # Empty array
                self._record_field(path, 'array', [], parent_type, note="Empty array")
            else:
                # Record array field
                self._record_field(path, 'array', f"[{len(obj)} items]", parent_type)

                # Analyze ALL items in array
                for idx, item in enumerate(obj):
                    item_path = f"{path}[{idx}]"
                    self.extract_fields_recursive(item, item_path, parent_type)

        elif isinstance(obj, bool):
            self._record_field(path, 'boolean', obj, parent_type)

        elif isinstance(obj, (int, float)):
            self._record_field(path, 'number', obj, parent_type)

        elif isinstance(obj, str):
            self._record_field(path, 'string', obj, parent_type)

        else:
            self._record_field(path, type(obj).__name__, str(obj), parent_type)

    def _record_field(self, path: str, field_type: str, value: Any, parent_type: str = None, note: str = None):
        """Record a field with its metadata."""
        if path not in self.all_fields:
            self.all_fields[path] = {
                'json_path': path,
                'type': field_type,
                'values': [],
                'parent_type': parent_type,
                'note': note
            }
            self.total_fields += 1

        # Collect value
        field_info = self.all_fields[path]
        if value is not None and value not in field_info['values']:
            # Limit examples to prevent huge lists
            if len(field_info['values']) < 100:
                field_info['values'].append(value)

    def analyze_items(self):
        """Analyze all items in the items[] array, grouped by type."""
        items = self.character_data.get('items', [])
        self.total_items = len(items)

        print(f"\nAnalyzing {self.total_items} items...")

        for idx, item in enumerate(items):
            item_type = item.get('type', 'unknown')
            item_name = item.get('name', f'Item {idx}')

            # Count this type
            self.item_types[item_type]['count'] += 1

            # Store example
            if len(self.item_types[item_type]['examples']) < 5:
                self.item_types[item_type]['examples'].append(item_name)

            # Extract all fields recursively with type context
            self.extract_fields_recursive(item, f"items[{idx}]", parent_type=item_type)

        print(f"[OK] Found {len(self.item_types)} different item types")
        for itype, info in sorted(self.item_types.items()):
            print(f"  - {itype}: {info['count']} items")

    def analyze_top_level(self):
        """Analyze top-level character fields (excluding items array)."""
        print("\nAnalyzing top-level character data...")

        for key, value in self.character_data.items():
            if key == 'items':
                # Items are analyzed separately
                continue
            self.extract_fields_recursive(value, key, parent_type='character')

        print(f"[OK] Analyzed top-level structure")

    def calculate_statistics(self):
        """Calculate statistics for numeric fields."""
        for path, field_info in self.all_fields.items():
            if field_info['type'] == 'number' and field_info['values']:
                numeric_values = [v for v in field_info['values'] if isinstance(v, (int, float))]
                if numeric_values:
                    field_info['min'] = min(numeric_values)
                    field_info['max'] = max(numeric_values)
                    field_info['often_zero'] = numeric_values.count(0) / len(numeric_values) > 0.5

    def load_formulas(self):
        """Load calculation formulas from reference_data/formulas.json."""
        formulas_file = Path('reference_data/formulas.json')
        if formulas_file.exists():
            with open(formulas_file, 'r', encoding='utf-8') as f:
                self.formulas = json.load(f)
        else:
            print(f"Warning: {formulas_file} not found. Skipping derived statistics calculation.")

    def calculate_derived_statistics(self):
        """Calculate all derived statistics using validated formulas."""
        if not self.formulas:
            print("Skipping derived statistics calculation (no formulas loaded)")
            return

        system = self.character_data.get('system', {})

        # Extract attributes
        attrs = system.get('attributes', {})
        STR = attrs.get('str', {}).get('value', 0)
        PER = attrs.get('per', {}).get('value', 0)
        END = attrs.get('end', {}).get('value', 0)
        CHA = attrs.get('cha', {}).get('value', 0)
        INT = attrs.get('int', {}).get('value', 0)
        AGI = attrs.get('agi', {}).get('value', 0)
        LCK = attrs.get('luc', {}).get('value', 0)

        # Extract other needed values
        level = system.get('level', {}).get('value', 1)
        radiation = system.get('radiation', 0)
        well_rested = system.get('conditions', {}).get('wellRested', False)

        # Bonuses
        health_bonus = system.get('health', {}).get('bonus', 0)
        defense_bonus = system.get('defense', {}).get('bonus', 0)
        initiative_bonus = system.get('initiative', {}).get('bonus', 0)
        melee_damage_bonus = system.get('meleeDamage', {}).get('bonus', 0)
        carry_weight_mod = system.get('carryWeight', {}).get('mod', 0)

        # Calculate Max Health
        max_health = END + LCK + (level - 1) - radiation + health_bonus + (2 if well_rested else 0)

        # Calculate Defense
        defense = (2 if AGI >= 9 else 1) + defense_bonus

        # Calculate Initiative
        initiative = PER + AGI + initiative_bonus

        # Calculate Melee Damage
        if STR >= 11:
            melee_damage = 3
        elif STR >= 9:
            melee_damage = 2
        elif STR >= 7:
            melee_damage = 1
        else:
            melee_damage = 0
        melee_damage += melee_damage_bonus

        # Calculate Carry Weight
        carry_weight_base = 150  # Default from formulas.json
        carry_weight_total = carry_weight_base + (STR * 10) + carry_weight_mod

        # Calculate Next Level XP
        next_level = level + 1
        next_level_xp = (next_level * (next_level - 1) // 2) * 100

        # Store calculated values
        self.calculated_stats = {
            'max_health': {
                'calculated': max_health,
                'stored': system.get('health', {}).get('max', 0),
                'formula': 'END + LCK + (Level-1) - Radiation + health_bonus + (wellRested ? 2 : 0)',
                'components': {
                    'END': END,
                    'LCK': LCK,
                    'level': level,
                    'radiation': radiation,
                    'health_bonus': health_bonus,
                    'well_rested': well_rested
                }
            },
            'defense': {
                'calculated': defense,
                'stored': system.get('defense', {}).get('value', 0),
                'formula': 'AGI <= 8 ? 1 : 2 (+ bonus)',
                'components': {
                    'AGI': AGI,
                    'defense_bonus': defense_bonus
                }
            },
            'initiative': {
                'calculated': initiative,
                'stored': system.get('initiative', {}).get('value', 0),
                'formula': 'PER + AGI + bonus',
                'components': {
                    'PER': PER,
                    'AGI': AGI,
                    'initiative_bonus': initiative_bonus
                }
            },
            'melee_damage': {
                'calculated': melee_damage,
                'stored': system.get('meleeDamage', {}).get('value', 0),
                'formula': 'STR 7-8: +1, STR 9-10: +2, STR 11+: +3 (+ bonus)',
                'components': {
                    'STR': STR,
                    'melee_damage_bonus': melee_damage_bonus
                }
            },
            'carry_weight': {
                'calculated': carry_weight_total,
                'stored': system.get('carryWeight', {}).get('total', 0),
                'formula': '150 + (STR × 10) + mod',
                'components': {
                    'base': carry_weight_base,
                    'STR': STR,
                    'carry_weight_mod': carry_weight_mod
                }
            },
            'next_level_xp': {
                'calculated': next_level_xp,
                'stored': system.get('level', {}).get('nextLevelXP', 0),
                'formula': '(Level × (Level-1) / 2) × 100',
                'components': {
                    'current_level': level,
                    'next_level': next_level
                }
            }
        }

        print(f"\n[Calculated Derived Statistics]")
        for stat_name, stat_data in self.calculated_stats.items():
            match = "[OK]" if stat_data['calculated'] == stat_data['stored'] or stat_data['stored'] == 0 else "[MISMATCH]"
            print(f"  {stat_name}: {stat_data['calculated']} (stored: {stat_data['stored']}) {match}")

    def categorize_fields(self) -> Dict[str, List[str]]:
        """
        Categorize fields into logical groups for FIELD_INVENTORY.md.
        Based on DATA_ANALYSIS.md structure.
        """
        categories = {
            'Character Basic Information': [],
            'S.P.E.C.I.A.L. Attributes': [],
            'Derived Statistics': [],
            'Body Parts': [],
            'Conditions & Status': [],
            'Currency & Materials': [],
            'Level & XP': [],
            'Metadata': [],
            'Items - Skills': [],
            'Items - Perks': [],
            'Items - Traits': [],
            'Items - Weapons': [],
            'Items - Ammo': [],
            'Items - Apparel': [],
            'Items - Apparel Mods': [],
            'Items - Consumables': [],
            'Items - Books & Magazines': [],
            'Items - Miscellany': [],
            'Effects': [],
            'Other': []
        }

        for path in self.all_fields.keys():
            # Top-level character info
            if path in ['name', 'type', 'img']:
                categories['Character Basic Information'].append(path)
            elif path.startswith('system.biography') or path.startswith('system.origin') or \
                 path.startswith('system.description') or path.startswith('system.trait') or \
                 path.startswith('system.complication'):
                categories['Character Basic Information'].append(path)

            # S.P.E.C.I.A.L.
            elif path.startswith('system.attributes.'):
                categories['S.P.E.C.I.A.L. Attributes'].append(path)

            # Derived stats
            elif any(path.startswith(f'system.{stat}') for stat in
                    ['health', 'defense', 'initiative', 'meleeDamage', 'carryWeight', 'resistance']):
                categories['Derived Statistics'].append(path)

            # Body parts
            elif path.startswith('system.body_parts.'):
                categories['Body Parts'].append(path)

            # Conditions
            elif path.startswith('system.conditions') or path.startswith('system.immunities'):
                categories['Conditions & Status'].append(path)

            # Level & XP
            elif path.startswith('system.level') or 'XP' in path:
                categories['Level & XP'].append(path)

            # Currency & Materials
            elif path.startswith('system.currency') or path.startswith('system.materials'):
                categories['Currency & Materials'].append(path)

            # Items by type
            elif 'items[' in path:
                # Determine item type from path
                # Extract index and check item type
                if any(f'[{i}]' in path for i in range(self.total_items)):
                    # Find which item type this belongs to
                    for idx in range(self.total_items):
                        if f'items[{idx}]' in path:
                            item = self.character_data['items'][idx]
                            item_type = item.get('type', 'unknown')

                            if item_type == 'skill':
                                categories['Items - Skills'].append(path)
                            elif item_type == 'perk':
                                categories['Items - Perks'].append(path)
                            elif item_type == 'trait':
                                categories['Items - Traits'].append(path)
                            elif item_type == 'weapon':
                                categories['Items - Weapons'].append(path)
                            elif item_type == 'ammo':
                                categories['Items - Ammo'].append(path)
                            elif item_type == 'apparel':
                                categories['Items - Apparel'].append(path)
                            elif item_type == 'apparel_mod':
                                categories['Items - Apparel Mods'].append(path)
                            elif item_type == 'consumable':
                                categories['Items - Consumables'].append(path)
                            elif item_type == 'books_and_magz':
                                categories['Items - Books & Magazines'].append(path)
                            elif item_type == 'miscellany':
                                categories['Items - Miscellany'].append(path)
                            else:
                                categories['Other'].append(path)
                            break

            # Effects
            elif path.startswith('effects'):
                categories['Effects'].append(path)

            # Metadata
            elif path.startswith('_stats') or path.startswith('flags') or path.startswith('prototypeToken') or \
                 path.startswith('folder') or path.startswith('sort') or path.startswith('ownership'):
                categories['Metadata'].append(path)

            # Radiation, other system fields
            elif path.startswith('system.radiation') or path.startswith('system.bodyType'):
                categories['Derived Statistics'].append(path)

            # Everything else
            else:
                categories['Other'].append(path)

        # Remove empty categories
        return {k: v for k, v in categories.items() if v}

    def generate_json_output(self) -> dict:
        """Generate machine-readable JSON output."""
        output = {
            'meta': {
                'analyzed_character': self.character_name,
                'character_type': self.character_type,
                'character_level': self.character_level,
                'character_file': str(self.character_file),
                'analyzed_date': datetime.now().isoformat(),
                'total_fields': self.total_fields,
                'total_items': self.total_items
            },
            'fields': {
                path: {
                    'json_path': info['json_path'],
                    'type': info['type'],
                    'values': info['values'][:10],  # Limit to 10 examples
                    'value_count': len(info['values']),
                    'min': info.get('min'),
                    'max': info.get('max'),
                    'often_zero': info.get('often_zero', False),
                    'parent_type': info.get('parent_type'),
                    'note': info.get('note')
                }
                for path, info in sorted(self.all_fields.items())
            },
            'item_types': {
                itype: {
                    'count': info['count'],
                    'examples': info['examples']
                }
                for itype, info in sorted(self.item_types.items())
            }
        }

        # Add calculated statistics if available
        if self.calculated_stats:
            output['calculated_statistics'] = self.calculated_stats

        return output

    def generate_markdown_output(self) -> str:
        """Generate human-readable Markdown output."""
        categories = self.categorize_fields()

        md = f"""# Complete Field Inventory

**Character**: {self.character_name}
**Type**: {self.character_type}
**Level**: {self.character_level}
**Analyzed**: {datetime.now().strftime('%Y-%m-%d %H:%M')}

**Statistics**:
- Total Fields: {self.total_fields}
- Total Items: {self.total_items}
- Item Types: {len(self.item_types)}

---

## Item Type Summary

| Item Type | Count | Examples |
|-----------|-------|----------|
"""

        for itype, info in sorted(self.item_types.items()):
            examples = ', '.join(info['examples'][:3])
            md += f"| {itype} | {info['count']} | {examples} |\n"

        md += "\n---\n\n"

        # Add calculated statistics section
        if self.calculated_stats:
            md += "## Calculated Derived Statistics\n\n"
            md += "These values are calculated from character attributes using validated formulas.\n\n"
            md += "| Statistic | Calculated | Stored in JSON | Formula | Status |\n"
            md += "|-----------|------------|----------------|---------|--------|\n"

            for stat_name, stat_data in self.calculated_stats.items():
                calculated = stat_data['calculated']
                stored = stat_data['stored']
                formula = stat_data['formula']

                if stored == 0:
                    status = "✓ Calculated (stored as 0)"
                elif calculated == stored:
                    status = "✓ Match"
                else:
                    status = f"⚠ MISMATCH"

                md += f"| {stat_name.replace('_', ' ').title()} | {calculated} | {stored} | `{formula}` | {status} |\n"

            md += "\n**Component Values:**\n\n"
            for stat_name, stat_data in self.calculated_stats.items():
                md += f"- **{stat_name.replace('_', ' ').title()}**: "
                components = ', '.join([f"{k}={v}" for k, v in stat_data['components'].items()])
                md += f"{components}\n"

            md += "\n---\n\n"

        # Generate categorized field tables
        for category, paths in categories.items():
            if not paths:
                continue

            md += f"## {category}\n\n"
            md += "| JSON Path | Type | Examples | Min | Max | Notes |\n"
            md += "|-----------|------|----------|-----|-----|-------|\n"

            for path in sorted(paths):
                info = self.all_fields[path]

                # Format examples
                examples = info['values'][:3] if info['values'] else []
                if info['type'] == 'string':
                    # Truncate long strings
                    examples = [str(v)[:50] + '...' if len(str(v)) > 50 else str(v) for v in examples]
                examples_str = '<br>'.join([f"`{v}`" for v in examples])

                # Min/Max
                min_val = info.get('min', '')
                max_val = info.get('max', '')

                # Notes
                notes = []
                if info.get('often_zero'):
                    notes.append('Often 0')
                if info.get('note'):
                    notes.append(info['note'])
                notes_str = '<br>'.join(notes)

                md += f"| `{path}` | {info['type']} | {examples_str} | {min_val} | {max_val} | {notes_str} |\n"

            md += "\n"

        return md

    def run(self):
        """Run complete analysis."""
        print(f"\n{'='*60}")
        print(f"Fallout Character JSON Analyzer")
        print(f"{'='*60}\n")

        # Load
        self.load_character()
        self.load_formulas()

        # Analyze
        self.analyze_top_level()
        self.analyze_items()
        self.calculate_statistics()

        # Calculate derived statistics
        if self.formulas:
            print(f"\nCalculating derived statistics...")
            self.calculate_derived_statistics()

        print(f"\n{'='*60}")
        print(f"Analysis Complete!")
        print(f"{'='*60}")
        print(f"Total Fields Extracted: {self.total_fields}")
        print(f"Total Items Analyzed: {self.total_items}")
        print(f"Item Types Found: {len(self.item_types)}")

        # Generate outputs
        print(f"\nGenerating outputs...")

        # JSON
        json_output = self.generate_json_output()
        json_file = Path('extracted_fields.json')
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(json_output, f, indent=2, ensure_ascii=False)
        print(f"[OK] Generated: {json_file}")

        # Markdown
        md_output = self.generate_markdown_output()
        md_file = Path('FIELD_INVENTORY.md')
        with open(md_file, 'w', encoding='utf-8') as f:
            f.write(md_output)
        print(f"[OK] Generated: {md_file}")

        print(f"\n{'='*60}")
        print(f"Done! [OK]")
        print(f"{'='*60}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python analyze_character.py <character_json_file>")
        print("\nExample:")
        print("  python analyze_character.py fvtt_export/fvtt-Actor-dr.-eloise-'ellie'-harper-jkTOphZz7Tvl7Qqn.json")
        sys.exit(1)

    character_file = Path(sys.argv[1])

    if not character_file.exists():
        print(f"Error: File not found: {character_file}")
        sys.exit(1)

    analyzer = CharacterAnalyzer(character_file)
    analyzer.run()


if __name__ == '__main__':
    main()
