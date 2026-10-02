"""Deterministic, distinct output names for actor exports."""

from hashlib import sha256
import os
from pathlib import Path
from tempfile import NamedTemporaryFile

from lib.character_data import Character
from lib.utils import sanitize_filename


def sheet_path(character: Character, output_dir: Path, format_type: str,
               appendix: bool = False) -> Path:
    """Name sheets by display name and source filename to avoid actor collisions."""
    if format_type not in ('html', 'markdown'):
        raise ValueError(f"Unsupported format: {format_type}")
    source = Path(character.character_file).name
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

    temporary = None
    try:
        with NamedTemporaryFile(mode='w', encoding='utf-8', dir=path.parent,
                                prefix='.sheet-', delete=False) as output:
            temporary = Path(output.name)
            output.write(content)
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)
