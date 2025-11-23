#!/usr/bin/env python3
"""
Fallout Character Sheet Generator

Generates comprehensive Markdown character sheets from FVTT Fallout character JSON exports.
Includes all stats, skills, perks, equipment, and descriptions needed for offline gameplay.

Usage:
    python generate_character_sheet.py <character_json_file>
    python generate_character_sheet.py fvtt_export/fvtt-Actor-dr.-eloise-'ellie'-harper-jkTOphZz7Tvl7Qqn.json
"""

import json
import sys
from pathlib import Path
from typing import Any, Dict, List
from datetime import datetime
import re


class CharacterSheetGenerator:
    """Generates Markdown character sheets from FVTT Fallout character JSON."""

    def __init__(self, character_file: Path):
        self.character_file = character_file
        self.character_data = None
        self.character_name = None
        self.character_type = None
        self.character_level = None
        self.formulas = None
        self.derived_stats = {}

    def load_character(self):
        """Load character JSON file."""
        print(f"Loading character: {self.character_file}")
        with open(self.character_file, 'r', encoding='utf-8') as f:
            self.character_data = json.load(f)

        self.character_name = self.character_data.get('name', 'Unknown')
        self.character_type = self.character_data.get('type', 'Unknown')
        self.character_level = self.character_data.get('system', {}).get('level', {}).get('value', '?')

        print(f"[OK] Loaded: {self.character_name} (Type: {self.character_type}, Level: {self.character_level})")

    def load_formulas(self):
        """Load calculation formulas from reference_data/formulas.json."""
        formulas_file = Path('reference_data/formulas.json')
        if formulas_file.exists():
            with open(formulas_file, 'r', encoding='utf-8') as f:
                self.formulas = json.load(f)
            print("[OK] Loaded formulas")
        else:
            print(f"Warning: {formulas_file} not found.")

    def calculate_derived_statistics(self):
        """Calculate all derived statistics using validated formulas."""
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
        carry_weight_base = 150
        carry_weight_total = carry_weight_base + (STR * 10) + carry_weight_mod

        # Calculate Next Level XP
        next_level = level + 1
        next_level_xp = (next_level * (next_level - 1) // 2) * 100

        # Store calculated values
        self.derived_stats = {
            'max_health': max_health,
            'current_health': system.get('health', {}).get('value', max_health),
            'defense': defense,
            'initiative': initiative,
            'melee_damage': melee_damage,
            'carry_weight_total': carry_weight_total,
            'carry_weight_current': system.get('carryWeight', {}).get('value', 0),
            'next_level_xp': next_level_xp,
            'current_xp': system.get('level', {}).get('currentXP', 0),
            'radiation': radiation,
            'well_rested': well_rested
        }

        print(f"[OK] Calculated derived statistics")

    def strip_html(self, text: str) -> str:
        """Remove HTML tags from text."""
        if not text:
            return ""
        # Remove HTML tags
        clean = re.sub(r'<[^>]+>', '', text)
        # Decode HTML entities
        clean = clean.replace('&nbsp;', ' ')
        clean = clean.replace('&lt;', '<')
        clean = clean.replace('&gt;', '>')
        clean = clean.replace('&amp;', '&')
        return clean.strip()

    def format_description(self, text: str, indent: int = 0) -> str:
        """Format description text with proper indentation."""
        if not text:
            return ""

        clean = self.strip_html(text)
        # Add indentation
        indent_str = " " * indent
        lines = clean.split('\n')
        return '\n'.join([f"{indent_str}{line.strip()}" for line in lines if line.strip()])

    def generate_header(self) -> str:
        """Generate character sheet header."""
        system = self.character_data.get('system', {})
        origin = system.get('origin', '')

        md = f"""# {self.character_name}

**Origin**: {origin}
**Level**: {self.character_level} | **XP**: {self.derived_stats['current_xp']} / {self.derived_stats['next_level_xp']}

---

"""
        return md

    def generate_special_attributes(self) -> str:
        """Generate S.P.E.C.I.A.L. attributes section."""
        system = self.character_data.get('system', {})
        attrs = system.get('attributes', {})

        md = "## S.P.E.C.I.A.L. Attributes\n\n"
        md += "| Attribute | Value |\n"
        md += "|-----------|-------|\n"
        md += f"| **Strength** | {attrs.get('str', {}).get('value', 0)} |\n"
        md += f"| **Perception** | {attrs.get('per', {}).get('value', 0)} |\n"
        md += f"| **Endurance** | {attrs.get('end', {}).get('value', 0)} |\n"
        md += f"| **Charisma** | {attrs.get('cha', {}).get('value', 0)} |\n"
        md += f"| **Intelligence** | {attrs.get('int', {}).get('value', 0)} |\n"
        md += f"| **Agility** | {attrs.get('agi', {}).get('value', 0)} |\n"
        md += f"| **Luck** | {attrs.get('luc', {}).get('value', 0)} |\n\n"

        return md

    def generate_derived_stats(self) -> str:
        """Generate derived statistics section."""
        md = "## Derived Statistics\n\n"
        md += "| Statistic | Value |\n"
        md += "|-----------|-------|\n"
        md += f"| **Health** | {self.derived_stats['current_health']} / {self.derived_stats['max_health']} |\n"
        md += f"| **Defense** | {self.derived_stats['defense']} |\n"
        md += f"| **Initiative** | {self.derived_stats['initiative']} |\n"
        md += f"| **Melee Damage** | +{self.derived_stats['melee_damage']} |\n"
        md += f"| **Carry Weight** | {self.derived_stats['carry_weight_current']} / {self.derived_stats['carry_weight_total']} lbs |\n"
        md += f"| **Radiation** | {self.derived_stats['radiation']} |\n\n"

        return md

    def generate_skills(self) -> str:
        """Generate skills section."""
        items = self.character_data.get('items', [])
        skills = [item for item in items if item.get('type') == 'skill']

        if not skills:
            return ""

        md = "## Skills\n\n"
        md += "| Skill | Tag | Rank | Attribute |\n"
        md += "|-------|-----|------|------------|\n"

        for skill in sorted(skills, key=lambda s: s.get('name', '')):
            name = skill.get('name', 'Unknown')
            rank = skill.get('system', {}).get('value', 0)
            tag_field = skill.get('system', {}).get('tag', False)
            # Handle both boolean and object formats
            if isinstance(tag_field, bool):
                tag_value = tag_field
            else:
                tag_value = tag_field.get('value', False) if isinstance(tag_field, dict) else False
            tag = "✓" if tag_value else ""
            attribute = skill.get('system', {}).get('defaultAttribute', '')

            md += f"| {name} | {tag} | {rank} | {attribute.upper() if attribute else ''} |\n"

        md += "\n"
        return md

    def generate_perks(self) -> str:
        """Generate perks section."""
        items = self.character_data.get('items', [])
        perks = [item for item in items if item.get('type') == 'perk']

        if not perks:
            return ""

        md = "## Perks\n\n"

        for perk in sorted(perks, key=lambda p: p.get('name', '')):
            name = perk.get('name', 'Unknown')
            rank = perk.get('system', {}).get('rank', {}).get('value', 1)
            description = perk.get('system', {}).get('description', '')
            requirements = perk.get('system', {}).get('requirements', '')

            if rank > 1:
                md += f"### {name} (Rank {rank})\n\n"
            else:
                md += f"### {name}\n\n"

            if description:
                md += f"{self.format_description(description)}\n\n"

            if requirements:
                req_clean = self.strip_html(requirements)
                md += f"**Requirements**: {req_clean}\n\n"

        return md

    def generate_trait(self) -> str:
        """Generate trait section."""
        items = self.character_data.get('items', [])
        traits = [item for item in items if item.get('type') == 'trait']

        if not traits:
            return ""

        md = "## Trait\n\n"

        for trait in traits:
            name = trait.get('name', 'Unknown')
            description = trait.get('system', {}).get('description', '')

            md += f"### {name}\n\n"
            if description:
                md += f"{self.format_description(description)}\n\n"

        return md

    def generate_weapons(self) -> str:
        """Generate weapons section with ammunition."""
        items = self.character_data.get('items', [])
        weapons = [item for item in items if item.get('type') == 'weapon']
        ammo = [item for item in items if item.get('type') == 'ammo']

        if not weapons and not ammo:
            return ""

        md = "## Weapons\n\n"

        # Weapons
        for weapon in sorted(weapons, key=lambda w: w.get('name', '')):
            name = weapon.get('name', 'Unknown')
            system = weapon.get('system', {})

            damage = system.get('damage', {}).get('rating', 0)
            damage_type = system.get('damage', {}).get('type', '')
            qualities = system.get('qualities', '')
            effects = system.get('effects', '')
            fire_rate = system.get('fireRate', 0)
            range_val = system.get('range', '')

            md += f"### {name}\n\n"
            md += f"- **Damage**: {damage} ({damage_type})\n"
            if fire_rate:
                md += f"- **Fire Rate**: {fire_rate}\n"
            if range_val:
                md += f"- **Range**: {range_val}\n"
            if qualities:
                md += f"- **Qualities**: {self.strip_html(qualities)}\n"
            if effects:
                md += f"- **Effects**: {self.strip_html(effects)}\n"
            md += "\n"

        # Ammunition
        if ammo:
            md += "### Ammunition\n\n"
            md += "| Ammo Type | Quantity |\n"
            md += "|-----------|----------|\n"
            for item in sorted(ammo, key=lambda a: a.get('name', '')):
                name = item.get('name', 'Unknown')
                quantity = item.get('system', {}).get('quantity', 1)
                md += f"| {name} | {quantity} |\n"
            md += "\n"

        return md

    def generate_apparel(self) -> str:
        """Generate apparel section."""
        items = self.character_data.get('items', [])
        apparel_items = [item for item in items if item.get('type') == 'apparel']

        if not apparel_items:
            return ""

        md = "## Apparel\n\n"

        for item in sorted(apparel_items, key=lambda a: a.get('name', '')):
            name = item.get('name', 'Unknown')
            system = item.get('system', {})

            description = system.get('description', '')
            locations = system.get('location', {})
            resistance = system.get('resistance', {})

            md += f"### {name}\n\n"

            # Show locations
            covered_parts = [part.upper() for part, val in locations.items() if val]
            if covered_parts:
                md += f"**Covers**: {', '.join(covered_parts)}\n\n"

            # Show resistances
            res_parts = []
            if resistance.get('physical', 0):
                res_parts.append(f"Physical +{resistance['physical']}")
            if resistance.get('energy', 0):
                res_parts.append(f"Energy +{resistance['energy']}")
            if resistance.get('radiation', 0):
                res_parts.append(f"Radiation +{resistance['radiation']}")
            if resistance.get('poison', 0):
                res_parts.append(f"Poison +{resistance['poison']}")

            if res_parts:
                md += f"**Resistances**: {', '.join(res_parts)}\n\n"

            if description:
                md += f"{self.format_description(description)}\n\n"

        return md

    def generate_consumables(self) -> str:
        """Generate consumables section."""
        items = self.character_data.get('items', [])
        consumables = [item for item in items if item.get('type') == 'consumable']

        if not consumables:
            return ""

        md = "## Consumables\n\n"
        md += "| Item | Quantity | Effect |\n"
        md += "|------|----------|--------|\n"

        for item in sorted(consumables, key=lambda c: c.get('name', '')):
            name = item.get('name', 'Unknown')
            quantity = item.get('system', {}).get('quantity', 1)
            description = item.get('system', {}).get('description', '')
            desc_short = self.strip_html(description)[:80] + "..." if len(self.strip_html(description)) > 80 else self.strip_html(description)

            md += f"| {name} | {quantity} | {desc_short} |\n"

        md += "\n"
        return md

    def generate_gear(self) -> str:
        """Generate miscellaneous gear section."""
        items = self.character_data.get('items', [])
        misc_items = [item for item in items if item.get('type') in ['miscellany', 'books_and_magz']]

        if not misc_items:
            return ""

        md = "## Gear & Miscellany\n\n"

        for item in sorted(misc_items, key=lambda m: (m.get('type', ''), m.get('name', ''))):
            name = item.get('name', 'Unknown')
            item_type = item.get('type', '')
            quantity = item.get('system', {}).get('quantity', 1)
            description = item.get('system', {}).get('description', '')

            if item_type == 'books_and_magz':
                md += f"- **{name}** - Book/Magazine"
                if description:
                    md += f": {self.strip_html(description)[:100]}"
                md += "\n"
            else:
                md += f"- **{name}**"
                if quantity > 1:
                    md += f" (x{quantity})"
                if description:
                    desc_short = self.strip_html(description)[:100]
                    md += f": {desc_short}"
                    if len(self.strip_html(description)) > 100:
                        md += "..."
                md += "\n"

        md += "\n"
        return md

    def generate_body_status(self) -> str:
        """Generate body parts status section."""
        system = self.character_data.get('system', {})
        body_parts = system.get('body_parts', {})

        if not body_parts:
            return ""

        md = "## Body Status\n\n"
        md += "| Body Part | Status | Injuries | Resistances (P/E/R/Po) |\n"
        md += "|-----------|--------|----------|------------------------|\n"

        part_names = {
            'head': 'Head',
            'torso': 'Torso',
            'armL': 'Left Arm',
            'armR': 'Right Arm',
            'legL': 'Left Leg',
            'legR': 'Right Leg'
        }

        for part_key in ['head', 'torso', 'armL', 'armR', 'legL', 'legR']:
            if part_key not in body_parts:
                continue

            part = body_parts[part_key]
            name = part_names.get(part_key, part_key)
            status = part.get('status', 'healthy')
            injuries_open = part.get('injuryOpenCount', 0)
            injuries_treated = part.get('injuryTreatedCount', 0)

            resistance = part.get('resistance', {})
            res_p = resistance.get('physical', 0)
            res_e = resistance.get('energy', 0)
            res_r = resistance.get('radiation', 0)
            res_po = resistance.get('poison', 0)

            injury_str = f"{injuries_open} open, {injuries_treated} treated" if (injuries_open + injuries_treated) > 0 else "None"

            md += f"| {name} | {status.capitalize()} | {injury_str} | {res_p}/{res_e}/{res_r}/{res_po} |\n"

        md += "\n"
        return md

    def generate_addictions(self) -> str:
        """Generate addictions section."""
        # In FVTT, addictions might be tracked in system.addictions or as items
        # For now, create placeholder section
        md = "## Addictions\n\n"
        md += "*None*\n\n"
        return md

    def generate_diseases(self) -> str:
        """Generate diseases section."""
        # In FVTT, diseases might be tracked in system.diseases or as items
        # For now, create placeholder section
        md = "## Diseases\n\n"
        md += "*None*\n\n"
        return md

    def generate_data(self) -> str:
        """Generate character data section (biography, background info)."""
        system = self.character_data.get('system', {})
        biography = system.get('biography', '')

        if not biography:
            return ""

        md = "## Data\n\n"
        md += self.format_description(biography) + "\n\n"

        return md

    def generate_character_sheet(self) -> str:
        """Generate complete character sheet."""
        md = self.generate_header()
        md += self.generate_special_attributes()
        md += self.generate_derived_stats()
        md += self.generate_skills()
        md += self.generate_body_status()  # Moved after skills
        md += self.generate_perks()
        md += self.generate_trait()
        md += self.generate_weapons()  # Now includes ammunition
        md += self.generate_apparel()
        md += self.generate_consumables()
        md += self.generate_gear()  # No longer includes ammunition
        md += self.generate_addictions()  # New section
        md += self.generate_diseases()  # New section
        md += self.generate_data()  # Renamed from biography

        # Footer
        md += "---\n\n"
        md += f"*Character sheet generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n"
        md += "*Generated with [Fallout Character Management](https://github.com/hnsstrk/fallout_char_mngt)*\n"

        return md

    def run(self):
        """Run the character sheet generator."""
        print(f"\n{'='*60}")
        print(f"Fallout Character Sheet Generator")
        print(f"{'='*60}\n")

        # Load
        self.load_character()
        self.load_formulas()

        # Calculate
        self.calculate_derived_statistics()

        # Generate
        print(f"\nGenerating character sheet...")
        sheet = self.generate_character_sheet()

        # Save to character_sheets/ directory
        output_dir = Path('character_sheets')
        output_dir.mkdir(exist_ok=True)

        safe_name = self.character_name.lower().replace(' ', '_').replace('.', '').replace("'", '')
        output_file = output_dir / f"{safe_name}.md"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(sheet)

        print(f"[OK] Generated: {output_file}")
        print(f"\n{'='*60}")
        print(f"Done! [OK]")
        print(f"{'='*60}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python generate_character_sheet.py <character_json_file>")
        print("\nExample:")
        print("  python generate_character_sheet.py fvtt_export/fvtt-Actor-dr.-eloise-'ellie'-harper-jkTOphZz7Tvl7Qqn.json")
        sys.exit(1)

    character_file = Path(sys.argv[1])

    if not character_file.exists():
        print(f"Error: File not found: {character_file}")
        sys.exit(1)

    generator = CharacterSheetGenerator(character_file)
    generator.run()


if __name__ == '__main__':
    main()
