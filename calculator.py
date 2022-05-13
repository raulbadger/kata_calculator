class Calculator:

    def __init__(self):
        pass

    SEPARATOR = ','

    def add(self, input_numbers):
        if self.is_two_numbers(input_numbers):
            split_numbers = input_numbers.split(self.SEPARATOR)
            return int(split_numbers[0]) + int(split_numbers[1])
        elif input_numbers == '':
            return 0
        return int(input_numbers)

    def is_two_numbers(self, input_numbers):
        return self.SEPARATOR in input_numbers
