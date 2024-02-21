from StringCalculator.src import string_calculator
 ##https://www.youtube.com/watch?v=R1VYSFQcKsQ

class TestStringCalculator:
    def test_stringcalculator_should_return_zero_on_empty_string(self):
        assert string_calculator.add("") == 0
        assert string_calculator.add(None) == 0
        
    def test_stringcalculator_should_return_the_value_on_single_number(self):
        assert string_calculator.add("1") == 1  
         
    def test_stringcalculator_should_return_the_sum_of_numbers(self):
        assert string_calculator.add("1,2") == 3
        assert string_calculator.add("1,2,4") == 7
        
    def test_stringcalculator_should_return_the_sum_of_numbers_with_new_lines(self):
        assert string_calculator.add("1\n2,3") == 6
        # assert string_calculator.add("1,2,4") == 7