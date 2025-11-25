from pathlib import Path

def validate_path(file_path: Path, base_dir: str = 'fvtt_export') -> Path:
    """
    Validates that the given file path is within the allowed base directory.

    Args:
        file_path: The user-provided path to the file.
        base_dir: The directory that the file_path must be relative to.

    Returns:
        The resolved, absolute path if it is safe.

    Raises:
        ValueError: If the path is outside the allowed base directory
                    (Directory Traversal attempt).
    """
    # Resolve the absolute path of the base directory and the requested file
    base_path = Path(base_dir).resolve()
    resolved_path = file_path.resolve()

    # Check if the resolved path is within the base directory
    if base_path not in resolved_path.parents and base_path != resolved_path:
        raise ValueError(
            f"Security Error: Path '{file_path}' attempts to access files "
            f"outside of the allowed directory '{base_dir}'."
        )

    return resolved_path
