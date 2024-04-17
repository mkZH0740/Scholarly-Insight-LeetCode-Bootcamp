from typing import Any


def make_ok(value: Any):
    return {"status": True, "value": value}


def make_err(error: Any):
    return {"status": False, "error": error}
