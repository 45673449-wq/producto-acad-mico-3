import pytest
from src.fibonacci import fibonacci

def test_fibonacci_base_cases():
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1

def test_fibonacci_recursive():
    assert fibonacci(5) == 5
    assert fibonacci(6) == 8
    assert fibonacci(7) == 13

def test_fibonacci_invalid_input():
    with pytest.raises(ValueError):
        fibonacci(0)
    with pytest.raises(ValueError):
        fibonacci(-3)
