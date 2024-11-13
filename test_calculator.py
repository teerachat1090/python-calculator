import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-5, 2), -3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(1,9),-8)
        self.assertEqual(self.calc.subtract(1,-9),10)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,9),18)
        self.assertEqual(self.calc.multiply(5,-6),-30)

    def test_divide(self):
        self.assertEqual(self.calc.divide(-7,3),-2)
        self.assertEqual(self.calc.divide(5,0),0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(4,4),0)
        self.assertEqual(self.calc.modulo(-7,4),-3)

if __name__ == '__main__':
    unittest.main()