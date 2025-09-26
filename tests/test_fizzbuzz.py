import pytest
from src.fizzbuzz import fizzbuzz

def test_number_not_divisible():
    # Números que no son múltiplos de 3 ni de 5 deben devolverse como string
    assert fizzbuzz(1) == "1"
    assert fizzbuzz(2) == "2"

def test_divisible_by_three():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(6) == "Fizz"
    assert fizzbuzz(9) == "Fizz"

def test_divisible_by_five():
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(10) == "Buzz"
    assert fizzbuzz(20) == "Buzz"

def test_divisible_by_three_and_five():
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(30) == "FizzBuzz"
    assert fizzbuzz(45) == "FizzBuzz"

@pytest.mark.parametrize("n", [7, 11, 13])
def test_other_numbers(n):
    # Parametrización para probar varios casos de golpe
    assert fizzbuzz(n) == str(n)
