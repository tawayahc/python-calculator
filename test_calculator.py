import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, 2), 1)
        self.assertEqual(self.calc.add(1, -2), -1)
        self.assertEqual(self.calc.add(-1, -2), -3)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-5, 3), -8)
        self.assertEqual(self.calc.subtract(5, -3), 8)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-5, 3), -15)
        self.assertEqual(self.calc.multiply(5, -3), -15)
        self.assertEqual(self.calc.multiply(-5, -3), 15)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        self.assertEqual(self.calc.divide(0, 5), 0)
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)
        self.assertEqual(self.calc.modulo(-10, 3), -1)
        self.assertEqual(self.calc.modulo(10, -3), 1)
        self.assertEqual(self.calc.modulo(-10, -3), -1)
        self.assertEqual(self.calc.modulo(10, 5), 0)
        with self.assertRaises(ValueError):
            self.calc.modulo(10, 0)

if __name__ == '__main__':
    unittest.main()
