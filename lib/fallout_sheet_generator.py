#!/usr/bin/env python3
"""
Fallout Character Sheet Generator (Refactored)

Generates character sheets from FVTT Fallout JSON exports using the shared library.
Supports Markdown and HTML output formats.
"""

import sys
import argparse
from pathlib import Path
from datetime import datetime

# Import shared library components
from lib.character_data import Character
from lib.safe_path import validate_path
from lib.utils import sanitize_filename

# Optional dependency for HTML output
try:
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    JINJA2_AVAILABLE = True
except ImportError:
    JINJA2_AVAILABLE = False

class CharacterSheetGenerator:
    """Generates character sheets from a Character object."""

    def __init__(self, character: Character, output_format: str = 'markdown', include_appendix: bool = False):
        self.character = character
        self.output_format = output_format
        self.include_appendix = include_appendix
        self.template_dir = Path(__file__).parent.parent / 'templates'

    def generate_markdown_sheet(self) -> str:
        """Generates the full character sheet in Markdown format."""
        md = self._generate_header()
        md += self._generate_special_attributes()
        md += self._generate_derived_stats()
        md += self._generate_conditions()
        md += self._generate_body_status()
        md += self._generate_skills()
        md += self._generate_perks()

        trait = self.character.get_trait()
        if trait:
            md += self._generate_trait(trait)

        # Add placeholder sections for addictions and diseases
        md += "## Addictions\n\n*None*\n\n"
        md += "## Diseases\n\n*None*\n\n"

        md += self._generate_weapons_and_ammo()

        if self.character.type == 'robot':
            md += self._generate_robot_armor()
            md += self._generate_robot_mods()
        else:
            md += self._generate_apparel()

        md += self._generate_consumables()
        md += self._generate_gear()
        md += self._generate_data()
        md += self._generate_footer()

        return md

    def _generate_header(self) -> str:
        stats = self.character.derived_stats
        return (
            f"# {self.character.name}\n\n"
            f"**Origin**: {self.character.get_origin()}\n"
            f"**Level**: {self.character.level} | **XP**: {stats['current_xp']} / {stats['next_level_xp']}\n\n---\n\n"
        )

    def _generate_special_attributes(self) -> str:
        attrs = self.character.get_special_attributes()
        md = "## S.P.E.C.I.A.L. Attributes\n\n| Attribute | Value |\n|-----------|-------|\n"
        for name, value in attrs.items():
            md += f"| **{name}** | {value} |\n"
        return md + "\n"

    def _generate_derived_stats(self) -> str:
        stats = self.character.derived_stats
        md = "## Derived Statistics\n\n| Statistic | Value |\n|-----------|-------|\n"
        md += f"| **Health** | {stats['current_health']} / {stats['max_health']} |\n"
        md += f"| **Defense** | {stats['defense']} |\n"
        md += f"| **Initiative** | {stats['initiative']} |\n"
        md += f"| **Melee Damage** | +{stats['melee_damage']} |\n"
        md += f"| **Carry Weight** | {stats['carry_weight_current']} / {stats['carry_weight_total']} lbs |\n"
        md += f"| **Radiation** | {stats['radiation']} |\n\n"
        return md

    def _generate_conditions(self) -> str:
        conditions = self.character.get_conditions()
        md = "## Conditions\n\n| Condition | Value |\n|-----------|-------|\n"
        for name, value in conditions.items():
            md += f"| {name} | {'Yes' if isinstance(value, bool) and value else ('No' if isinstance(value, bool) else value)} |\n"
        return md + "\n"

    def _generate_body_status(self) -> str:
        parts = self.character.get_body_parts()
        md = "## Body Status\n\n| Body Part | Status | Injuries | Resistances (E/P/Po/R) |\n|-----------|--------|----------|------------------------|\n"
        for part in parts:
            injury_str = f"{part['injuries_open']} open, {part['injuries_treated']} treated" if (part['injuries_open'] + part['injuries_treated']) > 0 else "None"
            res_str = f"{part['energy_res']}/{part['physical_res']}/{part['poison_res']}/{part['radiation_res']}"
            md += f"| {part['name']} | {part['status']} | {injury_str} | {res_str} |\n"
        return md + "\n"

    def _generate_skills(self) -> str:
        skills = self.character.get_skills()
        md = "## Skills\n\n| Skill | Tag | Rank | Attribute | Description |\n|-------|-----|------|-----------|-------------|\n"
        for skill in skills:
            desc_oneline = ' '.join(skill['description'].splitlines())
            md += f"| {skill['name']} | {skill['tag']} | {skill['rank']} | {skill['attribute']} | {desc_oneline} |\n"
        return md + "\n"

    def _generate_perks(self) -> str:
        perks = self.character.get_perks()
        if not perks: return ""
        md = "## Perks\n\n"
        for perk in perks:
            md += f"### {perk['name']} (Rank {perk['rank']})\n\n"
            if perk['description']: md += f"{perk['description']}\n\n"
            if perk['requirements']: md += f"**Requirements**: {perk['requirements']}\n\n"
        return md

    def _generate_trait(self, trait: dict) -> str:
        if not trait: return ""
        return f"## Trait\n\n### {trait['name']}\n\n{trait['description']}\n\n"

    def _generate_weapons_and_ammo(self) -> str:
        weapons = self.character.get_weapons()
        ammo = self.character.get_ammo()
        if not weapons and not ammo: return ""

        md = "## Weapons\n\n"
        for w in weapons:
            md += f"### {w['name']}\n\n"
            md += f"- **Damage**: {w['damage']} ({w['damage_type']})\n"
            if w['fire_rate']: md += f"- **Fire Rate**: {w['fire_rate']}\n"
            if w['range']: md += f"- **Range**: {w['range']}\n"
            if w['qualities']: md += f"- **Qualities**: {w['qualities']}\n"
            if w['effects']: md += f"- **Effects**: {w['effects']}\n"
            if w['description']: md += f"\n{w['description']}\n"
            md += "\n"

        if ammo:
            md += "### Ammunition\n\n"
            for a in ammo:
                md += f"**{a['name']}** (x{a['quantity']})\n\n"
                if a['description']: md += f"{a['description']}\n\n"
        return md

    def _generate_apparel(self) -> str:
        apparel = self.character.get_apparel()
        if not apparel: return ""
        md = "## Apparel\n\n"
        for item in apparel:
            md += f"### {item['name']}\n\n"
            if item['locations']: md += f"**Covers**: {item['locations']}\n\n"
            if item['resistances']: md += f"**Resistances**: {item['resistances']}\n\n"
            if item['description']: md += f"{item['description']}\n\n"
        return md

    def _generate_robot_armor(self) -> str:
        armor = self.character.get_robot_armor()
        if not armor: return ""
        md = "## Robot Armor\n\n"
        for item in armor:
            md += f"### {item['name']}{' ✓' if item['equipped'] else ''}\n\n"
            res = item['resistance']
            res_parts = [f"{res_type.capitalize()} +{val}" for res_type, val in res.items() if val > 0]
            if res_parts: md += f"**Resistances**: {', '.join(res_parts)}\n\n"
            if item['description']: md += f"{item['description']}\n\n"
        return md

    def _generate_robot_mods(self) -> str:
        mods = self.character.get_robot_mods()
        if not mods: return ""
        md = "## Robot Modules\n\n"
        for item in mods:
            md += f"### {item['name']}{' ✓' if item['equipped'] else ''}\n\n"
            if item['effect']: md += f"**Effect**: {item['effect']}\n\n"
            if item['description']: md += f"{item['description']}\n\n"
        return md

    def _generate_consumables(self) -> str:
        items = self.character.get_consumables()
        if not items: return ""
        md = "## Consumables\n\n"
        for item in items:
            md += f"### {item['name']} (x{item['quantity']})\n\n"
            if item['description']: md += f"{item['description']}\n\n"
        return md

    def _generate_gear(self) -> str:
        items = self.character.get_misc_gear()
        if not items: return ""
        md = "## Gear & Miscellany\n\n"
        for item in items:
            md += f"### {item['name']} (x{item['quantity']}){' - Book/Magazine' if item['is_book'] else ''}\n\n"
            if item['description']: md += f"{item['description']}\n\n"
        return md

    def _generate_data(self) -> str:
        bio = self.character.get_biography()
        if not bio: return ""
        return f"## Data\n\n{bio}\n\n"

    def _generate_footer(self) -> str:
        return (
            "---\n\n"
            f"*Character sheet generated on {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n"
            "*Generated with [Fallout Character Management](https://github.com/hnsstrk/fallout_char_mngt)*\n"
        )

    def generate_html_sheet(self) -> str:
        """Generates the full character sheet in HTML format."""
        if not JINJA2_AVAILABLE:
            raise RuntimeError("HTML output requires jinja2. Install with: pip install jinja2")

        env = Environment(
            loader=FileSystemLoader(self.template_dir),
            autoescape=select_autoescape(['html', 'xml']) # Enable autoescaping for security
        )
        template = env.get_template('character_sheet.html')

        context = {
            'character': self.character,
            'attributes': self.character.get_special_attributes(),
            'derived': self.character.derived_stats,
            'conditions': self.character.get_conditions(),
            'body_parts': self.character.get_body_parts(),
            'skills': self.character.get_skills(),
            'perks': self.character.get_perks(),
            'trait': self.character.get_trait(),
            'weapons': self.character.get_weapons(),
            'ammo': self.character.get_ammo(),
            'apparel': self.character.get_apparel(),
            'robot_armor': self.character.get_robot_armor(),
            'robot_mods': self.character.get_robot_mods(),
            'consumables': self.character.get_consumables(),
            'gear': self.character.get_misc_gear(),
            'is_robot': self.character.type == 'robot',
            'biography': self.character.get_biography(),
            'generated_date': datetime.now().strftime('%Y-%m-%d %H:%M'),
            'include_appendix': self.include_appendix
        }
        return template.render(context)

def main():
    parser = argparse.ArgumentParser(
        description='Generate character sheets from FVTT Fallout JSON exports.',
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('character_file', type=Path, help='Path to FVTT character JSON file')
    parser.add_argument('--format', '-f', choices=['markdown', 'html'], default='markdown', help='Output format')
    parser.add_argument('--appendix', action='store_true', help='Include appendix with skill descriptions (HTML only)')
    args = parser.parse_args()

    # Security check for Jinja2
    if args.format == 'html' and not JINJA2_AVAILABLE:
        print("Error: HTML output requires jinja2. Please install it.", file=sys.stderr)
        sys.exit(1)

    try:
        # Security: Validate the path before using it
        safe_file_path = validate_path(args.character_file, base_dir='fvtt_export')

        # Load character using the central library
        character = Character(safe_file_path)

        # Generate the sheet
        generator = CharacterSheetGenerator(character, args.format, args.appendix)

        if args.format == 'html':
            sheet_content = generator.generate_html_sheet()
            extension = 'html'
        else:
            sheet_content = generator.generate_markdown_sheet()
            extension = 'md'

        # Save the output file
        output_dir = Path('character_sheets')
        output_dir.mkdir(exist_ok=True)
        safe_name = sanitize_filename(character.name)
        output_file = output_dir / f"{safe_name}.{extension}"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(sheet_content)

        print(f"Successfully generated character sheet: {output_file}")

    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()
