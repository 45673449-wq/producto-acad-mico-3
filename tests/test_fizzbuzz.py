from src.fizzbuzz import fizzbuzz

def test_returns_number_as_string():
    assert fizzbuzz(1) == "1"

def test_returns_fizz_when_multiple_of_three():
    assert fizzbuzz(3) == "Fizz"

def test_returns_buzz_when_multiple_of_five():
    assert fizzbuzz(5) == "Buzz"

def test_returns_fizzbuzz_when_multiple_of_three_and_five():
    assert fizzbuzz(15) == "FizzBuzz"
