from calculator import Calculator
import pytest

def test_add():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_divide():
    calc = Calculator()
    assert calc.divide(10, 2) == 5.0
