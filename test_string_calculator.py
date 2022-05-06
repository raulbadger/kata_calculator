import unittest

from calculator import Calculator


class MyTestCase(unittest.TestCase):


    def test_given_a_string_calculator_class_when_is_called_with_empty_string_then_it_returns_0(self):
        input_parameter = ''
        expected_output = 0
        calculator = Calculator()

        actual_output = calculator.add(input_parameter)
        self.assertEqual(expected_output, actual_output)

    def test_given_a_string_calculator_class_when_is_called_with_one_number_then_it_returns_the_same_number(self):
        input_parameter = '7'
        expected_output = 7
        calculator = Calculator()

        actual_output = calculator.add(input_parameter)
        self.assertEqual(expected_output, actual_output)

    def test_given_a_string_calculator_class_when_is_called_with_two_numbers_then_it_returns_the_add_of_the_numbers(self):
        input_parameter = '7,3'
        expected_output = 10
        calculator = Calculator()

        actual_output = calculator.add(input_parameter)
        self.assertEqual(expected_output, actual_output)
