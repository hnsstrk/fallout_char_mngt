"""
Shared utility functions for the character sheet generator.
"""
import re

def sanitize_filename(name: str) -> str:
    """
    Sanitizes a string to be used as a valid filename.

    - Transliterates common special characters (umlauts, accents).
    - Allows alphanumeric characters, spaces, and underscores.
    - Removes leading/trailing whitespace.
    - Replaces spaces with underscores.
    - Converts to lowercase.
    - Falls back to 'unnamed_character' if result is empty.

    Args:
        name: The string to sanitize.

    Returns:
        A sanitized, filename-safe string.
    """
    # Transliterate common special characters
    replacements = {
        'ä': 'ae', 'ö': 'oe', 'ü': 'ue', 'ß': 'ss',
        'Ä': 'Ae', 'Ö': 'Oe', 'Ü': 'Ue',
        'é': 'e', 'è': 'e', 'ê': 'e', 'ë': 'e',
        'á': 'a', 'à': 'a', 'â': 'a',
        'í': 'i', 'ì': 'i', 'î': 'i',
        'ó': 'o', 'ò': 'o', 'ô': 'o',
        'ú': 'u', 'ù': 'u', 'û': 'u',
    }
    for char, replacement in replacements.items():
        name = name.replace(char, replacement)
    # Allow alphanumeric, space, and underscore
    sanitized = "".join(c for c in name if c.isalnum() or c in (' ', '_'))
    # Replace spaces with underscores and convert to lowercase
    sanitized = sanitized.strip().replace(' ', '_').lower()
    # Fallback for empty result
    if not sanitized:
        sanitized = "unnamed_character"
    return sanitized
