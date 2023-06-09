import pytest
import re


def validate_password(password: str):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password) or not re.search(r"[a-z]", password) or not re.search(r"\d", password):
        return False
    if re.search(r"[^A-Za-z0-9]", password):
        return False
    return True

@pytest.mark.parametrize("password, expected_result", [
    ("tomY2005", True),
    ("tomY200#", False),
    ("tomyasis", False),
    ("TOMYAS1S", False),
    ("70314212", False),
])

def test_validate_password(password, expected_result):
    assert validate_password(password) == expected_result
