from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, List, Any, Optional

class SystemInterface(ABC):
    """
    Abstract Base Class for RPG System Handlers.
    Each game system (Fallout, etc.) must implement this interface.
    """

    @property
    @abstractmethod
    def system_name(self) -> str:
        """Return the display name of the system."""
        pass

    @abstractmethod
    def can_handle(self, file_path: Path, data: dict) -> bool:
        """
        Check if the file/data belongs to this system.
        """
        pass

    @abstractmethod
    def load_character(self, file_path: Path) -> Any:
        """
        Load a character from a file.
        Returns a character object specific to the system (or a wrapper).
        """
        pass

    @abstractmethod
    def validate(self, character: Any) -> Dict[str, List[str]]:
        """
        Validate the character.
        Returns a dictionary with keys 'errors' and 'warnings' (or similar categories).
        Example: {'errors': ['Invalid Level'], 'warnings': ['Missing Bio']}
        """
        pass

    @abstractmethod
    def get_character_info(self, character: Any) -> Dict[str, str]:
        """
        Return basic info for list display.
        Expected keys: 'name', 'class' (or 'level'/'origin'), 'system'.
        """
        pass

    @abstractmethod
    def generate_sheet(self, character: Any, format_type: str, options: Dict[str, Any] = None) -> str:
        """
        Generate a character sheet.
        format_type: 'markdown', 'html'
        options: extra flags like 'appendix'
        Returns the content of the sheet as a string.
        """
        pass
