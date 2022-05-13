class Calculator:

    def __init__(self):
        pass

    SEPARATOR = ','

    def add(self, input_numbers):
        if self.is_two_numbers(input_numbers):
            split_numbers = input_numbers.split(self.SEPARATOR)
            result = 0
            for number in split_numbers:
                result += int(number)
            return result
        elif input_numbers == '':
            return 0
        return int(input_numbers)

    def is_two_numbers(self, input_numbers):
        return self.SEPARATOR in input_numbers
