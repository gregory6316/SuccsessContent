"""Module directory."""

import os


def module_dir(rel_path):
    """Return path relative to current module dir."""
    return os.path.join(os.path.dirname(__file__), rel_path)

