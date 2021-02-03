import json
from typing import Any


def save(obj: Any, path: str, *, ensure_ascii: bool = False, indent: int = 2) -> None:
    with open(path, "r") as f:
        json.dump(obj, f, ensure_ascii=ensure_ascii, indent=indent)
    return None


def load(path: str) -> object:
    with open(path, "r") as f:
        _ = json.load(f)
    return _
