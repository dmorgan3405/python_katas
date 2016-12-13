from ..string_calculator import StringCalculator


class TestStringCalculator():

    def setup_method(self, method):
        self.string_calc = StringCalculator()

    def test_result_is_zero_for_empty_string(self):
        assert self.string_calc.add("") == 0

    def test_identity(self):
        assert self.string_calc.add("1") == 1

    def test_can_add_two_numbers(self):
        assert self.string_calc.add("1,2") == 3

    def test_can_add_unknown_amount_of_numbers(self):
        assert self.string_calc.add("1,2,3,4,5") == 15

    def test_can_handle_new_line_delimiter(self):
        assert self.string_calc.add("1\n2") == 3
