"""
Shared utility functions for the character sheet generator.
"""
import re

def sanitize_filename(name: str) -> str:
    """
    Sanitizes a string to be used as a valid filename.

    - Allows alphanumeric characters, spaces, and underscores.
    - Removes leading/trailing whitespace.
    - Replaces spaces with underscores.
    - Converts to lowercase.

    Args:
        name: The string to sanitize.

    Returns:
        A sanitized, filename-safe string.
    """
    # Allow alphanumeric, space, and underscore
    sanitized = "".join(c for c in name if c.isalnum() or c in (' ', '_'))
    # Replace spaces with underscores and convert to lowercase
    sanitized = sanitized.strip().replace(' ', '_').lower()
    return sanitized
