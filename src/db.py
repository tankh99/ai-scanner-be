import json
from pathlib import Path

DATA_DIR = Path("data")
VALUE_FILE = DATA_DIR / 'value.json'

DATA_DIR.mkdir(exist_ok=True)


def read_value():
    try:
        if VALUE_FILE.exists():
            with open(VALUE_FILE, 'r') as f:
                data = json.load(f)
                return data
        return None
    except Exception as e:
        print(f"Error reading value: {e}")
        return None

def write_value(data):
    try:
        with open(VALUE_FILE, 'w') as f:
            print(type(data), data)
            json.dump(data.model_dump(), f)
        return True
    except Exception as e:
        print(f"Error writing value: {e}")
        return False
