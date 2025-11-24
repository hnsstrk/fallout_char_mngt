#!/usr/bin/env python3
"""
Fallout Character Sheet Generator

Generates comprehensive character sheets from FVTT Fallout character JSON exports.
Supports Markdown and HTML output formats.
Includes all stats, skills, perks, equipment, and descriptions needed for offline gameplay.

Usage:
    python generate_character_sheet.py <character_json_file> [--format FORMAT]
    python generate_character_sheet.py fvtt_export/character.json --format html

Formats:
    markdown (default) - Plain text Markdown file
    html               - Styled HTML file (B&W print optimized, requires jinja2)
"""

import json
import sys
import argparse
from pathlib import Path
from typing import Any, Dict, List
from datetime import datetime
import re

# Optional dependency for HTML output
try:
    from jinja2 import Environment, FileSystemLoader
    JINJA2_AVAILABLE = True
except ImportError:
    JINJA2_AVAILABLE = False


class CharacterSheetGenerator:
    """Generates character sheets from FVTT Fallout character JSON.

    Supports multiple output formats:
    - markdown: Plain text Markdown (default, no dependencies)
    - html: Styled HTML with CSS (requires jinja2)
    """

    def __init__(self, character_file: Path, output_format: str = 'markdown'):
        self.character_file = character_file
        self.output_format = output_format
        self.character_data = None
        self.character_name = None
        self.character_type = None
        self.character_level = None
        self.formulas = None
        self.derived_stats = {}

        # Template directory for HTML output
        self.template_dir = Path(__file__).parent / 'templates'

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
        """Generate skills section as table with descriptions."""
        items = self.character_data.get('items', [])
        skills = [item for item in items if item.get('type') == 'skill']

        if not skills:
            return ""

        md = "## Skills\n\n"
        md += "| Skill | Tag | Rank | Attribute | Description |\n"
        md += "|-------|-----|------|-----------|-------------|\n"

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
            description = skill.get('system', {}).get('description', '')

            # Clean description for table cell - remove HTML and newlines
            desc_clean = self.strip_html(description) if description else ""
            # Replace newlines with spaces to keep table intact
            desc_clean = desc_clean.replace('\n', ' ').replace('\r', ' ')
            # Remove multiple spaces
            desc_clean = ' '.join(desc_clean.split())

            md += f"| {name} | {tag} | {rank} | {attribute.upper() if attribute else ''} | {desc_clean} |\n"

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
        """Generate weapons section with ammunition and descriptions."""
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
            description = system.get('description', '')

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

            if description:
                md += f"\n{self.format_description(description)}\n"

            md += "\n"

        # Ammunition
        if ammo:
            md += "### Ammunition\n\n"

            for item in sorted(ammo, key=lambda a: a.get('name', '')):
                name = item.get('name', 'Unknown')
                quantity = item.get('system', {}).get('quantity', 1)
                description = item.get('system', {}).get('description', '')

                md += f"**{name}** (x{quantity})\n\n"

                if description:
                    md += f"{self.format_description(description)}\n\n"

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
        """Generate consumables section with full descriptions."""
        items = self.character_data.get('items', [])
        consumables = [item for item in items if item.get('type') == 'consumable']

        if not consumables:
            return ""

        md = "## Consumables\n\n"

        for item in sorted(consumables, key=lambda c: c.get('name', '')):
            name = item.get('name', 'Unknown')
            quantity = item.get('system', {}).get('quantity', 1)
            description = item.get('system', {}).get('description', '')

            md += f"### {name}"
            if quantity > 1:
                md += f" (x{quantity})"
            md += "\n\n"

            if description:
                md += f"{self.format_description(description)}\n\n"

        return md

    def generate_gear(self) -> str:
        """Generate miscellaneous gear section with full descriptions."""
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

            md += f"### {name}"
            if quantity > 1:
                md += f" (x{quantity})"

            if item_type == 'books_and_magz':
                md += " - Book/Magazine"

            md += "\n\n"

            if description:
                md += f"{self.format_description(description)}\n\n"

        return md

    def generate_conditions(self) -> str:
        """Generate conditions section."""
        system = self.character_data.get('system', {})
        conditions = system.get('conditions', {})

        if not conditions:
            return ""

        md = "## Conditions\n\n"
        md += "| Condition | Value |\n"
        md += "|-----------|-------|\n"

        # Extract condition values
        hunger = conditions.get('hunger', 0)
        thirst = conditions.get('thirst', 0)
        sleep = conditions.get('sleep', 0)
        fatigue = conditions.get('fatigue', 0)
        intoxication = conditions.get('intoxication', 0)
        alcoholic = conditions.get('alcoholic', False)
        well_rested = conditions.get('wellRested', False)

        # Display conditions
        md += f"| Hunger | {hunger} |\n"
        md += f"| Thirst | {thirst} |\n"
        md += f"| Sleep | {sleep} |\n"
        md += f"| Fatigue | {fatigue} |\n"
        md += f"| Intoxication | {intoxication} |\n"
        md += f"| Alcoholic | {'Yes' if alcoholic else 'No'} |\n"
        md += f"| Well Rested | {'Yes' if well_rested else 'No'} |\n"

        md += "\n"
        return md

    def generate_body_status(self) -> str:
        """Generate body parts status section."""
        system = self.character_data.get('system', {})
        body_parts = system.get('body_parts', {})

        if not body_parts:
            return ""

        # Get global resistances (e.g., from Supermutant origin)
        global_resistance = system.get('resistance', {})
        global_p = global_resistance.get('physical', 0)
        global_e = global_resistance.get('energy', 0)
        global_r = global_resistance.get('radiation', 0)
        global_po = global_resistance.get('poison', 0)

        # Get immunities (robots have poison/radiation immunity)
        immunities = system.get('immunities', {})
        immune_poison = immunities.get('poison', False)
        immune_radiation = immunities.get('radiation', False)

        # Calculate resistances from equipped apparel/robot_armor for each body part
        items = self.character_data.get('items', [])
        # Include both apparel (humanoids) and robot_armor (robots)
        apparel_items = [item for item in items if item.get('type') in ['apparel', 'robot_armor']]

        # Initialize equipment resistance tracking per body part
        equipment_resistance = {
            'head': {'physical': 0, 'energy': 0, 'radiation': 0, 'poison': 0},
            'torso': {'physical': 0, 'energy': 0, 'radiation': 0, 'poison': 0},
            'armL': {'physical': 0, 'energy': 0, 'radiation': 0, 'poison': 0},
            'armR': {'physical': 0, 'energy': 0, 'radiation': 0, 'poison': 0},
            'legL': {'physical': 0, 'energy': 0, 'radiation': 0, 'poison': 0},
            'legR': {'physical': 0, 'energy': 0, 'radiation': 0, 'poison': 0}
        }

        # Sum up resistances from all equipped apparel
        for item in apparel_items:
            item_system = item.get('system', {})
            if not item_system.get('equipped', False):
                continue

            resistance = item_system.get('resistance', {})
            location = item_system.get('location', {})

            # Apply this apparel's resistance to all covered body parts
            for part_key, is_covered in location.items():
                if is_covered and part_key in equipment_resistance:
                    equipment_resistance[part_key]['physical'] += resistance.get('physical', 0)
                    equipment_resistance[part_key]['energy'] += resistance.get('energy', 0)
                    equipment_resistance[part_key]['radiation'] += resistance.get('radiation', 0)
                    equipment_resistance[part_key]['poison'] += resistance.get('poison', 0)

        md = "## Body Status\n\n"
        md += "| Body Part | Status | Injuries | Resistances (E/P/Po/R) |\n"
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

            # Combine all three sources: body part + global + equipment
            part_resistance = part.get('resistance', {})
            equip_res = equipment_resistance[part_key]

            res_p = part_resistance.get('physical', 0) + global_p + equip_res['physical']
            res_e = part_resistance.get('energy', 0) + global_e + equip_res['energy']
            res_r = part_resistance.get('radiation', 0) + global_r + equip_res['radiation']
            res_po = part_resistance.get('poison', 0) + global_po + equip_res['poison']

            # Apply immunities (robots are immune to poison/radiation)
            if immune_radiation:
                res_r = 999
            if immune_poison:
                res_po = 999

            # Convert 999+ to infinity symbol (immune)
            def fmt_res(val: int) -> str:
                return '∞' if val >= 999 else str(val)

            injury_str = f"{injuries_open} open, {injuries_treated} treated" if (injuries_open + injuries_treated) > 0 else "None"

            md += f"| {name} | {status.capitalize()} | {injury_str} | {fmt_res(res_e)}/{fmt_res(res_p)}/{fmt_res(res_po)}/{fmt_res(res_r)} |\n"

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
        md += self.generate_conditions()
        md += self.generate_body_status()
        md += self.generate_skills()
        md += self.generate_perks()
        md += self.generate_trait()
        md += self.generate_addictions()  # Before weapons
        md += self.generate_diseases()  # Before weapons
        md += self.generate_weapons()  # Now includes ammunition
        md += self.generate_apparel()
        md += self.generate_consumables()
        md += self.generate_gear()
        md += self.generate_data()

        # Footer
        md += "---\n\n"
        md += f"*Character sheet generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n"
        md += "*Generated with [Fallout Character Management](https://github.com/hnsstrk/fallout_char_mngt)*\n"

        return md

    # ===== HTML OUTPUT METHODS =====

    def _extract_conditions(self, system: Dict) -> Dict:
        """Extract conditions for template."""
        conditions = system.get('conditions', {})
        return {
            'hunger': conditions.get('hunger', 0),
            'thirst': conditions.get('thirst', 0),
            'sleep': conditions.get('sleep', 0),
            'fatigue': conditions.get('fatigue', 0),
            'intoxication': conditions.get('intoxication', 0),
            'alcoholic': conditions.get('alcoholic', False),
            'well_rested': conditions.get('wellRested', False),
        }

    def _extract_body_parts(self, system: Dict, items: List) -> List[Dict]:
        """Extract body parts with combined resistances for template."""
        body_parts_data = system.get('body_parts', {})
        global_res = system.get('resistance', {})

        # Check for robot armor (provides immunities)
        robot_armor = system.get('robotArmor', {})

        # Calculate equipment resistances per body part
        equip_res = {part: {'physical': 0, 'energy': 0, 'radiation': 0, 'poison': 0}
                     for part in ['head', 'torso', 'armL', 'armR', 'legL', 'legR']}

        for item in items:
            if item.get('type') != 'apparel':
                continue
            item_sys = item.get('system', {})
            if not item_sys.get('equipped', False):
                continue
            res = item_sys.get('resistance', {})
            loc = item_sys.get('location', {})
            for part_key, is_covered in loc.items():
                if is_covered and part_key in equip_res:
                    equip_res[part_key]['physical'] += res.get('physical', 0)
                    equip_res[part_key]['energy'] += res.get('energy', 0)
                    equip_res[part_key]['radiation'] += res.get('radiation', 0)
                    equip_res[part_key]['poison'] += res.get('poison', 0)

        part_names = {
            'head': 'Head', 'torso': 'Torso', 'armL': 'Left Arm',
            'armR': 'Right Arm', 'legL': 'Left Leg', 'legR': 'Right Leg'
        }

        result = []
        for part_key in ['head', 'torso', 'armL', 'armR', 'legL', 'legR']:
            if part_key not in body_parts_data:
                continue
            part = body_parts_data[part_key]
            part_res = part.get('resistance', {})
            eq = equip_res[part_key]

            # Calculate total resistances
            phys = part_res.get('physical', 0) + global_res.get('physical', 0) + eq['physical']
            energy = part_res.get('energy', 0) + global_res.get('energy', 0) + eq['energy']
            rad = part_res.get('radiation', 0) + global_res.get('radiation', 0) + eq['radiation']
            poison = part_res.get('poison', 0) + global_res.get('poison', 0) + eq['poison']

            # Add robot armor immunities if present
            if robot_armor:
                phys += robot_armor.get('physical', 0)
                energy += robot_armor.get('energy', 0)
                rad += robot_armor.get('radiation', 0)
                poison += robot_armor.get('poison', 0)

            # Convert 999+ to infinity symbol (immune)
            def fmt_res(val: int) -> str:
                return '∞' if val >= 999 else str(val)

            result.append({
                'name': part_names.get(part_key, part_key),
                'status': part.get('status', 'healthy').capitalize(),
                'physical': fmt_res(phys),
                'energy': fmt_res(energy),
                'radiation': fmt_res(rad),
                'poison': fmt_res(poison),
            })

        return result

    def _extract_skills(self, items: List) -> List[Dict]:
        """Extract skills for template."""
        skills = [item for item in items if item.get('type') == 'skill']
        result = []
        for skill in sorted(skills, key=lambda s: s.get('name', '')):
            tag_field = skill.get('system', {}).get('tag', False)
            if isinstance(tag_field, bool):
                is_tagged = tag_field
            else:
                is_tagged = bool(tag_field)

            desc = skill.get('system', {}).get('description', '')
            result.append({
                'name': skill.get('name', 'Unknown'),
                'rank': skill.get('system', {}).get('value', 0),
                'attribute': skill.get('system', {}).get('defaultAttribute', '').upper(),
                'tag': is_tagged,
                'description': self.strip_html(desc) if desc else '',
            })
        return result

    def _extract_perks(self, items: List) -> List[Dict]:
        """Extract perks for template."""
        perks = [item for item in items if item.get('type') == 'perk']
        result = []
        for perk in sorted(perks, key=lambda p: p.get('name', '')):
            desc = perk.get('system', {}).get('description', '')
            result.append({
                'name': perk.get('name', 'Unknown'),
                'rank': perk.get('system', {}).get('rank', 1),
                'description': self.strip_html(desc) if desc else '',
            })
        return result

    def _extract_traits(self, items: List) -> List[Dict]:
        """Extract traits for template."""
        traits = [item for item in items if item.get('type') == 'trait']
        result = []
        for trait in traits:
            desc = trait.get('system', {}).get('description', '')
            result.append({
                'name': trait.get('name', 'Unknown'),
                'description': self.strip_html(desc) if desc else '',
            })
        return result

    def _extract_weapons(self, items: List) -> List[Dict]:
        """Extract weapons for template."""
        weapons = [item for item in items if item.get('type') == 'weapon']
        result = []
        for weapon in weapons:
            sys = weapon.get('system', {})
            damage = sys.get('damage', {})
            result.append({
                'name': weapon.get('name', 'Unknown'),
                'damage': damage.get('rating', 0),
                'damage_type': damage.get('damageType', '').upper()[:3],
                'range': sys.get('range', ''),
                'fire_rate': sys.get('fireRate', ''),
                'qualities': ', '.join(q.get('name', '') for q in sys.get('qualities', [])) or '',
            })
        return result

    def _extract_ammo(self, items: List) -> List[Dict]:
        """Extract ammunition for template."""
        ammo = [item for item in items if item.get('type') == 'ammo']
        return [{'name': a.get('name', ''), 'quantity': a.get('system', {}).get('quantity', 0)} for a in ammo]

    def _extract_apparel(self, items: List) -> List[Dict]:
        """Extract apparel for template."""
        apparel = [item for item in items if item.get('type') == 'apparel']
        result = []
        for item in apparel:
            sys = item.get('system', {})
            loc = sys.get('location', {})
            res = sys.get('resistance', {})

            locations = [k.replace('arm', 'Arm ').replace('leg', 'Leg ').replace('L', 'L').replace('R', 'R').title()
                         for k, v in loc.items() if v]
            resistances = f"E{res.get('energy', 0)}/P{res.get('physical', 0)}/Po{res.get('poison', 0)}/R{res.get('radiation', 0)}"

            result.append({
                'name': item.get('name', ''),
                'locations': ', '.join(locations),
                'resistances': resistances if any(res.values()) else '',
            })
        return result

    def _extract_consumables(self, items: List) -> List[Dict]:
        """Extract consumables for template."""
        consumables = [item for item in items if item.get('type') == 'consumable']
        result = []
        for item in consumables:
            desc = item.get('system', {}).get('description', '')
            result.append({
                'name': item.get('name', ''),
                'quantity': item.get('system', {}).get('quantity', 1),
                'description': self.strip_html(desc) if desc else '',
            })
        return result

    def _extract_gear(self, items: List) -> List[Dict]:
        """Extract gear and miscellany for template."""
        gear_types = ['miscellany', 'books_and_magz']
        gear = [item for item in items if item.get('type') in gear_types]
        result = []
        for item in gear:
            result.append({
                'name': item.get('name', ''),
                'quantity': item.get('system', {}).get('quantity', 1),
                'type_label': 'Book/Magazine' if item.get('type') == 'books_and_magz' else 'Misc',
            })
        return result

    def _prepare_template_context(self) -> Dict:
        """Prepare context dictionary for HTML template."""
        system = self.character_data.get('system', {})
        items = self.character_data.get('items', [])
        attrs = system.get('attributes', {})

        return {
            'character': {
                'name': self.character_name,
                'origin': system.get('origin', ''),
                'level': self.character_level,
            },
            'attributes': {
                'str': attrs.get('str', {}).get('value', 0),
                'per': attrs.get('per', {}).get('value', 0),
                'end': attrs.get('end', {}).get('value', 0),
                'cha': attrs.get('cha', {}).get('value', 0),
                'int': attrs.get('int', {}).get('value', 0),
                'agi': attrs.get('agi', {}).get('value', 0),
                'lck': attrs.get('luc', {}).get('value', 0),
            },
            'derived': self.derived_stats,
            'conditions': self._extract_conditions(system),
            'body_parts': self._extract_body_parts(system, items),
            'skills': self._extract_skills(items),
            'perks': self._extract_perks(items),
            'traits': self._extract_traits(items),
            'addictions': [],  # Placeholder
            'diseases': [],  # Placeholder
            'weapons': self._extract_weapons(items),
            'ammo': self._extract_ammo(items),
            'apparel': self._extract_apparel(items),
            'consumables': self._extract_consumables(items),
            'gear': self._extract_gear(items),
            'biography': self.strip_html(system.get('biography', '')),
            'generated_date': datetime.now().strftime('%Y-%m-%d %H:%M'),
        }

    def generate_html(self) -> str:
        """Generate HTML character sheet using Jinja2 template."""
        if not JINJA2_AVAILABLE:
            raise RuntimeError("HTML output requires jinja2. Install with: pip install jinja2")

        env = Environment(loader=FileSystemLoader(self.template_dir))
        template = env.get_template('character_sheet.html')
        context = self._prepare_template_context()
        return template.render(**context)

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

        # Generate based on format
        print(f"\nGenerating character sheet ({self.output_format})...")

        output_dir = Path('character_sheets')
        output_dir.mkdir(exist_ok=True)

        safe_name = self.character_name.lower().replace(' ', '_').replace('.', '').replace("'", '').replace('"', '')

        if self.output_format == 'html':
            sheet = self.generate_html()
            output_file = output_dir / f"{safe_name}.html"
        else:  # markdown (default)
            sheet = self.generate_character_sheet()
            output_file = output_dir / f"{safe_name}.md"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(sheet)

        print(f"[OK] Generated: {output_file}")
        print(f"\n{'='*60}")
        print(f"Done! [OK]")
        print(f"{'='*60}\n")


def main():
    parser = argparse.ArgumentParser(
        description='Generate character sheets from FVTT Fallout JSON exports.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  python generate_character_sheet.py fvtt_export/character.json
  python generate_character_sheet.py fvtt_export/character.json --format html
        '''
    )
    parser.add_argument('character_file', type=Path, help='Path to FVTT character JSON file')
    parser.add_argument('--format', '-f', choices=['markdown', 'html'], default='markdown',
                        help='Output format (default: markdown)')

    args = parser.parse_args()

    if not args.character_file.exists():
        print(f"Error: File not found: {args.character_file}")
        sys.exit(1)

    # Check dependencies for HTML
    if args.format == 'html' and not JINJA2_AVAILABLE:
        print("Error: HTML output requires jinja2. Install with: pip install jinja2")
        sys.exit(1)

    generator = CharacterSheetGenerator(args.character_file, args.format)
    generator.run()


if __name__ == '__main__':
    main()
