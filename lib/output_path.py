"""Deterministic, distinct output names for actor exports."""

from hashlib import sha256
import os
from pathlib import Path
from secrets import token_hex

from lib.character_data import Character
from lib.utils import sanitize_filename


def sheet_path(character: Character, output_dir: Path, format_type: str,
               appendix: bool = False) -> Path:
    """Name sheets by display name and resolved source path to avoid actor collisions."""
    if format_type not in ('html', 'markdown'):
        raise ValueError(f"Unsupported format: {format_type}")
    # Resolve so relative and absolute spellings of one export share a name.
    source = Path(character.character_file).resolve().as_posix()
    source_key = sha256(source.encode('utf-8')).hexdigest()[:12]
    name = sanitize_filename(character.name).encode('utf-8')[:100].decode('utf-8', errors='ignore')
    suffix = '-appendix' if format_type == 'html' and appendix else ''
    extension = 'html' if format_type == 'html' else 'md'
    return output_dir / f"{name}-{source_key}{suffix}.{extension}"


def write_sheet(path: Path, content: str, replace: bool = False) -> None:
    """Create exclusively, or atomically replace the path without following symlinks."""
    if not replace:
        with path.open('x', encoding='utf-8') as output:
            output.write(content)
        return

    # A new file gets the ordinary umask permissions, like the exclusive create above;
    # O_EXCL and O_NOFOLLOW keep a planted symlink from redirecting the write.
    temporary = path.parent / f".sheet-{token_hex(8)}"
    descriptor = os.open(temporary, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, 0o666)
    try:
        with open(descriptor, 'w', encoding='utf-8') as output:
            output.write(content)
        os.replace(temporary, path)
    finally:
        temporary.unlink(missing_ok=True)
