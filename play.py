#write me a function that peforms addition of two numbers

def add_numbers(a, b):
    return a + b

#now function that performs subtraction of two numbers
def subtract_numbers(a, b):
    return a - b

#function that performs multiplication of two numbers
def multiply_numbers(a, b):
    return a * b

#now write me unit tests for these functions
import unittest
class TestMathFunctions(unittest.TestCase):
    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(-1, 1), 0)
        self.assertEqual(add_numbers(0, 0), 0)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(5, 3), 2)
        self.assertEqual(subtract_numbers(0, 1), -1)
        self.assertEqual(subtract_numbers(-1, -1), 0)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(2, 3), 6)
        self.assertEqual(multiply_numbers(-1, 1), -1)
        self.assertEqual(multiply_numbers(0, 5), 0)