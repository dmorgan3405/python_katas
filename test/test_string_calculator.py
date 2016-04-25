import py.test
from python_katas.string_calculator.string_calculator import StringCalculator

def test_identity():
    calculator = StringCalculator()
    addends = "1"
    assert calculator.add(addends) == 1
