import pytest
from string_calculator import add

def test_empty_string_returns_0():
    assert add('') == 0