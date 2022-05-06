class Calculator:

    SEPARATOR = ','

    def add(self, input_numbers):
        if self.is_two_numbers(input_numbers):
            split_numbers = input_numbers.split(self.SEPARATOR)
            result = int(split_numbers[0]) + int(split_numbers[1])
        else:
            result = 0 if input_numbers == '' else int(input_numbers)

        return result

    def is_two_numbers(self, input_numbers):
        return self.SEPARATOR in input_numbers
