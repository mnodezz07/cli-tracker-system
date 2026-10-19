import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "database.json"


def load_data():
    """Load saved data or return empty collections."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        return {"users": [], "projects": [], "tasks": []}

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {"users": [], "projects": [], "tasks": []}


def save_data(data):
    """Save data to a JSON file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)