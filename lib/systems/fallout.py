from pathlib import Path
from typing import Dict, List, Any
import json
from lib.system_interface import SystemInterface
from lib.character_data import Character
from validate_character import CharacterValidator
from generate_character_sheet import CharacterSheetGenerator

class FalloutSystem(SystemInterface):
    """Handler for Fallout: The Roleplaying Game (FVTT export)."""

    @property
    def system_name(self) -> str:
        return "Fallout RPG"

    def can_handle(self, file_path: Path, data: dict) -> bool:
        # Check if it looks like a Fallout character
        # Usually checking "system" -> "game" identifier would be best, but FVTT exports vary.
        # Based on existing code, we assume if we can parse it with Character, it's ours.
        # But for quick check: look for "special" attributes in "system".
        system_data = data.get('system', {})
        return 'attributes' in system_data and 'str' in system_data['attributes']

    def load_character(self, file_path: Path) -> Character:
        return Character(file_path)

    def validate(self, character: Character) -> Dict[str, List[str]]:
        validator = CharacterValidator(character)
        validator.run_validation(verbose=False)
        return {
            'errors': validator.health_warnings,
            'warnings': validator.completeness_issues
        }

    def get_character_info(self, character: Character) -> Dict[str, str]:
        # For Fallout, we use Origin or Level as the "Class" equivalent
        origin = character.get_origin() or "Unknown Origin"
        return {
            'name': character.name,
            'class': f"Lvl {character.level} {origin}",
            'system': self.system_name
        }

    def generate_sheet(self, character: Character, format_type: str, options: Dict[str, Any] = None) -> str:
        if options is None:
            options = {}

        include_appendix = options.get('appendix', False)

        generator = CharacterSheetGenerator(character, output_format=format_type, include_appendix=include_appendix)

        if format_type == 'html':
            return generator.generate_html_sheet()
        elif format_type == 'markdown':
            return generator.generate_markdown_sheet()
        else:
            raise ValueError(f"Unsupported format: {format_type}")
