"""
VaultX: High-Velocity OSINT Infiltration Engine
Surpassing standard reconnaissance through deep-pivot interrogation.
"""

import pathlib
import json

__version__ = "1.0.1"
__author__  = "VaultX Dev Team"

# Elite Logic: Auto-load Data Stats on Import
def get_vector_counts():
    """Dynamically count the 1000+ vectors currently loaded in the vault."""
    data_path = pathlib.Path(__file__).parent / "data"
    counts = {}
    for filename in ["usernames.json", "emails.json", "phones.json", "domains.json"]:
        file_path = data_path / filename
        if file_path.exists():
            with open(file_path, 'r') as f:
                counts[filename.split('.')[0]] = len(json.load(f))
    return counts

# This makes the vector counts available to the CLI instantly
VECTOR_STATS = get_vector_counts()
