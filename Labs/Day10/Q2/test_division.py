import pytest
from calculator import divide

def test_division(sample_numbers, calculator_resource):
    a, b = sample_numbers
    assert divide(a, b) == 2

def test_division_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)
