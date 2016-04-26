import py.test
from python_katas.string_calculator.string_calculator import StringCalculator

def test_result_is_zero_for_empty_string():
    assert StringCalculator("").add() == 0

def test_identity():
    assert StringCalculator("1").add() == 1

def test_can_add_two_numbers():
    assert StringCalculator("1,2").add() == 3

def test_can_add_unknown_amount_of_numbers():
    assert StringCalculator("1,2,3,4,5").add() == 15

def test_can_handle_new_line_delimiter():
    assert StringCalculator("1\n2").add() == 3
