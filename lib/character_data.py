import html
import json
import re
from pathlib import Path
from typing import Any, Dict, List

class Character:
    """Represents a character, loading and parsing data from a JSON file."""

    def __init__(self, character_file: Path, data: dict = None):
        """
        Loads and initializes character data from a JSON file or a provided dict.

        Args:
            character_file: Path to the character's JSON export file.
            data: Optional pre-loaded character data dict. If provided, file loading is skipped.
        """
        self.character_file = character_file
        self.data = data if data is not None else self._load_character_data()

        self.name: str = self.data.get('name', 'Unknown')
        self.type: str = self.data.get('type', 'character')
        self.level: int = self.system.get('level', {}).get('value', 1)

        # Calculate derived statistics upon initialization
        self.derived_stats = self._calculate_derived_statistics()

    def _calculate_derived_statistics(self) -> Dict[str, Any]:
        """Calculates derived stats based on the character's core attributes."""
        attrs = self.system.get('attributes', {})
        STR = attrs.get('str', {}).get('value', 0)
        PER = attrs.get('per', {}).get('value', 0)
        END = attrs.get('end', {}).get('value', 0)
        AGI = attrs.get('agi', {}).get('value', 0)
        LCK = attrs.get('luc', {}).get('value', 0)

        radiation = self.system.get('radiation', 0)
        well_rested = self.system.get('conditions', {}).get('wellRested', False)

        # Bonuses and modifiers
        health_bonus = self.system.get('health', {}).get('bonus', 0)
        defense_bonus = self.system.get('defense', {}).get('bonus', 0)
        initiative_bonus = self.system.get('initiative', {}).get('bonus', 0)
        melee_damage_bonus = self.system.get('meleeDamage', {}).get('bonus', 0)
        carry_weight_mod = self.system.get('carryWeight', {}).get('mod', 0)

        # Calculations
        max_health = END + LCK + (self.level - 1) - radiation + health_bonus + (2 if well_rested else 0)
        defense = (2 if AGI >= 9 else 1) + defense_bonus
        initiative = PER + AGI + initiative_bonus

        if STR >= 11:
            melee_damage = 3
        elif STR >= 9:
            melee_damage = 2
        elif STR >= 7:
            melee_damage = 1
        else:
            melee_damage = 0
        melee_damage += melee_damage_bonus

        carry_weight_base = 150
        if self.type == 'robot':
            armor_carry_mod = sum(
                item.get('system', {}).get('carry', 0)
                for item in self.items
                if item.get('type') in ['robot_armor', 'robot_mod'] and item.get('system', {}).get('equipped', False)
            )
            carry_weight_total = carry_weight_base + carry_weight_mod + armor_carry_mod
        else:
            carry_weight_total = carry_weight_base + (STR * 10) + carry_weight_mod

        next_level = self.level + 1
        next_level_xp = (next_level * (next_level - 1) // 2) * 100

        return {
            'max_health': max_health,
            'current_health': self.system.get('health', {}).get('value', max_health),
            'defense': defense,
            'initiative': initiative,
            'melee_damage': melee_damage,
            'carry_weight_total': carry_weight_total,
            'carry_weight_current': self.system.get('carryWeight', {}).get('value', 0),
            'next_level_xp': next_level_xp,
            'current_xp': self.system.get('level', {}).get('currentXP', 0),
            'radiation': radiation,
            'well_rested': well_rested
        }

    @property
    def system(self) -> Dict[str, Any]:
        """Accessor for the 'system' part of the character data."""
        return self.data.get('system', {})

    def get_special_attributes(self) -> Dict[str, int]:
        """Returns a dictionary of S.P.E.C.I.A.L. attributes."""
        attrs = self.system.get('attributes', {})
        return {
            'Strength': attrs.get('str', {}).get('value', 0),
            'Perception': attrs.get('per', {}).get('value', 0),
            'Endurance': attrs.get('end', {}).get('value', 0),
            'Charisma': attrs.get('cha', {}).get('value', 0),
            'Intelligence': attrs.get('int', {}).get('value', 0),
            'Agility': attrs.get('agi', {}).get('value', 0),
            'Luck': attrs.get('luc', {}).get('value', 0),
        }

    def get_biography(self) -> str:
        """Returns the character's biography, cleaned of HTML."""
        bio = self.system.get('biography', '')
        return self.strip_html(bio)

    def get_origin(self) -> str:
        """Returns the character's origin."""
        return self.system.get('origin', '')

    def get_conditions(self) -> Dict[str, Any]:
        """Returns a dictionary of the character's current conditions."""
        conditions = self.system.get('conditions', {})
        return {
            'Hunger': conditions.get('hunger', 0),
            'Thirst': conditions.get('thirst', 0),
            'Sleep': conditions.get('sleep', 0),
            'Fatigue': conditions.get('fatigue', 0),
            'Intoxication': conditions.get('intoxication', 0),
            'Alcoholic': conditions.get('alcoholic', False),
            'Well Rested': conditions.get('wellRested', False),
        }

    def get_body_parts(self) -> List[Dict[str, Any]]:
        """
        Returns a list of body parts with their status and calculated resistances.
        Resistances are combined from body part, global, and equipped apparel sources.
        """
        body_parts_data = self.system.get('body_parts', {})
        if not body_parts_data:
            return []

        global_res = self.system.get('resistance', {})
        immunities = self.system.get('immunities', {})

        # Pre-calculate resistances from all equipped items for each body part
        equip_res = {part: {'physical': 0, 'energy': 0, 'radiation': 0, 'poison': 0}
                     for part in ['head', 'torso', 'armL', 'armR', 'legL', 'legR']}

        for item in self.get_items(type_filter=['apparel', 'robot_armor']):
            if not item.get('system', {}).get('equipped', False):
                continue

            res = item.get('system', {}).get('resistance', {})
            loc = item.get('system', {}).get('location', {})
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
        for part_key, part_data in body_parts_data.items():
            part_res = part_data.get('resistance', {})
            eq = equip_res.get(part_key, {})

            def calculate_resistance(res_type):
                val = (part_res.get(res_type, 0) +
                       global_res.get(res_type, 0) +
                       eq.get(res_type, 0))
                return '∞' if immunities.get(res_type, False) or val >= 999 else str(val)

            result.append({
                'name': part_names.get(part_key, part_key),
                'status': part_data.get('status', 'healthy').capitalize(),
                'injuries_open': part_data.get('injuryOpenCount', 0),
                'injuries_treated': part_data.get('injuryTreatedCount', 0),
                'physical_res': calculate_resistance('physical'),
                'energy_res': calculate_resistance('energy'),
                'radiation_res': calculate_resistance('radiation'),
                'poison_res': calculate_resistance('poison'),
            })
        return result

    @property
    def items(self) -> List[Dict[str, Any]]:
        """Accessor for the 'items' array."""
        return self.data.get('items', [])

    def get_items(self, type_filter: List[str] = None, sort_key: str = 'name') -> List[Dict[str, Any]]:
        """
        Retrieves a filtered and sorted list of items from the character data.

        Args:
            type_filter: A list of item types to include (e.g., ['weapon', 'apparel']).
                         If None, all items are returned.
            sort_key: The key to sort the items by. Defaults to 'name'.

        Returns:
            A list of item dictionaries.
        """
        items_to_process = self.items

        if type_filter:
            items_to_process = [item for item in items_to_process if item.get('type') in type_filter]

        return sorted(items_to_process, key=lambda i: i.get(sort_key, ''))

    def get_skills(self) -> List[Dict[str, Any]]:
        """Returns a formatted list of character skills."""
        skills_data = self.get_items(type_filter=['skill'])

        formatted_skills = []
        for skill in skills_data:
            system = skill.get('system', {})
            tag_field = system.get('tag', False)

            if isinstance(tag_field, bool):
                is_tagged = tag_field
            else:
                is_tagged = tag_field.get('value', False) if isinstance(tag_field, dict) else False

            formatted_skills.append({
                'name': skill.get('name', 'Unknown'),
                'rank': system.get('value', 0),
                'tag': "✓" if is_tagged else "",
                'attribute': system.get('defaultAttribute', '').upper(),
                'description': self.strip_html(system.get('description', ''))
            })
        return formatted_skills

    def get_perks(self) -> List[Dict[str, Any]]:
        """Returns a formatted list of character perks."""
        perks_data = self.get_items(type_filter=['perk'])
        return [
            {
                'name': perk.get('name', 'Unknown'),
                'rank': perk.get('system', {}).get('rank', {}).get('value', 1),
                'description': self.strip_html(perk.get('system', {}).get('description', '')),
                'requirements': self.strip_html(perk.get('system', {}).get('requirements', '')),
            }
            for perk in perks_data
        ]

    def get_trait(self) -> Dict[str, Any]:
        """Returns the character's trait, if any."""
        trait_data = self.get_items(type_filter=['trait'])
        if not trait_data:
            return None
        trait = trait_data[0]
        return {
            'name': trait.get('name', 'Unknown'),
            'description': self.strip_html(trait.get('system', {}).get('description', '')),
        }

    def get_weapons(self) -> List[Dict[str, Any]]:
        """Returns a formatted list of weapons."""
        weapons_data = self.get_items(type_filter=['weapon'])
        result = []
        for weapon in weapons_data:
            damage_data = weapon.get('system', {}).get('damage', {})

            # K5: Read damageType from structured object with booleans
            damage_type_obj = damage_data.get('damageType', {})
            damage_types = [k.capitalize() for k, v in damage_type_obj.items() if v]
            damage_type_str = '/'.join(damage_types) if damage_types else damage_data.get('type', '')

            # W2: Damage Effects (e.g. Piercing 1, Burst, Stun)
            damage_effect_obj = damage_data.get('damageEffect', {})
            damage_effects = []
            for effect, val in damage_effect_obj.items():
                if isinstance(val, dict):
                    # Structured format: {rank, value} — active when value > 0
                    if val.get('value', 0) > 0:
                        rank = val.get('rank', 0)
                        clean_name = effect.rstrip('_x').replace('_', ' ').capitalize()
                        if rank > 0 and effect.endswith('_x'):
                            damage_effects.append(f"{clean_name} {int(val['value'] * rank)}")
                        else:
                            damage_effects.append(clean_name)
                elif isinstance(val, bool) and val:
                    damage_effects.append(effect.replace('_', ' ').capitalize())
                elif isinstance(val, (int, float)) and val > 0:
                    clean_name = effect.rstrip('_x').replace('_', ' ').capitalize()
                    damage_effects.append(f"{clean_name} {int(val)}")

            # W2: Weapon Qualities (e.g. Accurate, Close Quarters, Reliable)
            weapon_quality_obj = damage_data.get('weaponQuality', {})
            weapon_qualities = []
            for quality, val in weapon_quality_obj.items():
                if isinstance(val, dict):
                    # Structured format: {rank, value} — active when value > 0
                    if val.get('value', 0) > 0:
                        rank = val.get('rank', 0)
                        clean_name = quality.rstrip('_x').replace('_', ' ').capitalize()
                        if rank > 0 and quality.endswith('_x'):
                            weapon_qualities.append(f"{clean_name} {int(val['value'] * rank)}")
                        else:
                            weapon_qualities.append(clean_name)
                elif isinstance(val, bool) and val:
                    weapon_qualities.append(quality.replace('_', ' ').replace(' x', '').capitalize())
                elif isinstance(val, (int, float)) and val > 0:
                    clean_name = quality.rstrip('_x').replace('_', ' ').capitalize()
                    weapon_qualities.append(f"{clean_name} {int(val)}")

            result.append({
                'name': weapon.get('name', 'Unknown'),
                'damage': damage_data.get('rating', 0),
                'damage_type': damage_type_str,
                'damage_effects': ', '.join(damage_effects) if damage_effects else '',
                'weapon_qualities': ', '.join(weapon_qualities) if weapon_qualities else '',
                'qualities': self.strip_html(weapon.get('system', {}).get('qualities', '')),
                'effects': self.strip_html(weapon.get('system', {}).get('effects', '')),
                'fire_rate': weapon.get('system', {}).get('fireRate', 0),
                'range': weapon.get('system', {}).get('range', ''),
                'description': self.strip_html(weapon.get('system', {}).get('description', '')),
            })
        return result

    def get_apparel(self) -> List[Dict[str, Any]]:
        """Returns a formatted list of apparel."""
        apparel_data = self.get_items(type_filter=['apparel'])
        results = []
        for item in apparel_data:
            system = item.get('system', {})
            locations = [part.upper() for part, val in system.get('location', {}).items() if val]
            resistance = system.get('resistance', {})
            res_parts = []
            if resistance.get('physical', 0): res_parts.append(f"Physical +{resistance['physical']}")
            if resistance.get('energy', 0): res_parts.append(f"Energy +{resistance['energy']}")
            if resistance.get('radiation', 0): res_parts.append(f"Radiation +{resistance['radiation']}")
            if resistance.get('poison', 0): res_parts.append(f"Poison +{resistance['poison']}")

            results.append({
                'name': item.get('name', 'Unknown'),
                'description': self.strip_html(system.get('description', '')),
                'locations': ", ".join(locations),
                'resistances': ", ".join(res_parts),
            })
        return results

    def get_robot_armor(self) -> List[Dict[str, Any]]:
        """Returns a formatted list of robot armor."""
        armor_data = self.get_items(type_filter=['robot_armor'])
        return [
            {
                'name': item.get('name', 'Unknown'),
                'description': self.strip_html(item.get('system', {}).get('description', '')),
                'equipped': item.get('system', {}).get('equipped', False),
                'resistance': item.get('system', {}).get('resistance', {}),
            }
            for item in armor_data
        ]

    def get_robot_mods(self) -> List[Dict[str, Any]]:
        """Returns a formatted list of robot mods."""
        mod_data = self.get_items(type_filter=['robot_mod'])
        return [
            {
                'name': item.get('name', 'Unknown'),
                'description': self.strip_html(item.get('system', {}).get('description', '')),
                'equipped': item.get('system', {}).get('equipped', False),
                'effect': self.strip_html(item.get('system', {}).get('effect', '')),
            }
            for item in mod_data
        ]

    def get_consumables(self) -> List[Dict[str, Any]]:
        """Returns a formatted list of consumables."""
        consumable_data = self.get_items(type_filter=['consumable'])
        return [
            {
                'name': item.get('name', 'Unknown'),
                'quantity': item.get('system', {}).get('quantity', 1),
                'description': self.strip_html(item.get('system', {}).get('description', '')),
            }
            for item in consumable_data
        ]

    def get_misc_gear(self) -> List[Dict[str, Any]]:
        """Returns a formatted list of miscellaneous gear."""
        gear_data = self.get_items(type_filter=['miscellany', 'books_and_magz'])
        return [
            {
                'name': item.get('name', 'Unknown'),
                'quantity': item.get('system', {}).get('quantity', 1),
                'description': self.strip_html(item.get('system', {}).get('description', '')),
                'is_book': item.get('type') == 'books_and_magz',
            }
            for item in gear_data
        ]

    def get_ammo(self) -> List[Dict[str, Any]]:
        """Returns a formatted list of ammunition."""
        ammo_data = self.get_items(type_filter=['ammo'])
        return [
            {
                'name': item.get('name', 'Unknown'),
                'quantity': item.get('system', {}).get('quantity', 1),
                'description': self.strip_html(item.get('system', {}).get('description', '')),
            }
            for item in ammo_data
        ]

    def get_luck_points(self) -> int:
        """Returns the character's current luck points."""
        return self.system.get('luckPoints', 0)

    def get_currency(self) -> Dict[str, int]:
        """Returns the character's currency (caps and other)."""
        currency = self.system.get('currency', {})
        return {
            'caps': currency.get('caps', 0),
            'other': currency.get('other', 0),
        }

    def get_addictions(self) -> List[Dict[str, Any]]:
        """Returns a list of the character's addictions."""
        addiction_data = self.get_items(type_filter=['addiction'])
        return [
            {
                'name': item.get('name', 'Unknown'),
                'description': self.strip_html(item.get('system', {}).get('description', '')),
            }
            for item in addiction_data
        ]

    def get_diseases(self) -> List[Dict[str, Any]]:
        """Returns a list of the character's diseases."""
        disease_data = self.get_items(type_filter=['disease'])
        return [
            {
                'name': item.get('name', 'Unknown'),
                'description': self.strip_html(item.get('system', {}).get('description', '')),
            }
            for item in disease_data
        ]

    def _load_character_data(self) -> Dict[str, Any]:
        """
        Loads character data from the specified JSON file.

        Returns:
            A dictionary containing the character data.

        Raises:
            FileNotFoundError: If the character file does not exist.
            json.JSONDecodeError: If the file is not valid JSON.
        """
        if not self.character_file.exists():
            raise FileNotFoundError(f"Character file not found: {self.character_file}")

        with open(self.character_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    @staticmethod
    def strip_html(text: str) -> str:
        """
        Removes HTML tags and decodes common entities from a string.

        Args:
            text: The input string, which may contain HTML.

        Returns:
            A cleaned string with HTML removed.
        """
        if not text:
            return ""
        # Remove HTML tags
        clean = re.sub(r'<[^>]+>', '', text)
        # Decode all HTML entities (including &uuml;, &auml;, etc.)
        clean = html.unescape(clean)
        return clean.strip()
