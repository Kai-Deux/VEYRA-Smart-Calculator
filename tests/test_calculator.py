
import unittest


from calculator import add, subtract, multiply, divide




class TestCalculator(unittest.TestCase):
    """Unit tests for the VEYRA arithmetic engine."""

    def test_addition(self):
        """Verify addition produces the expected result."""
        result = add(25, 15)
        self.assertEqual(result, 40)

    def test_subtraction(self):
        """Verify subtraction produces the expected result."""
        result = subtract(25, 15)
        self.assertEqual(result, 10)


    def test_multiplication(self):
        """Verify multiplication produces the expected result."""
        result = multiply(25, 4)
        self.assertEqual(result, 100)

    def test_division(self):
        """Verify division produces the expected result."""
        result = divide(100, 4)
        self.assertEqual(result, 25.0)

    def test_division_by_zero(self):
        """Verify division by zero raises ValueError."""
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_negative_numbers(self):
        """Verify arithmetic with negative numbers."""
        self.assertEqual(add(-10, 5), -5)
        self.assertEqual(subtract(-10, 5), -15)
        self.assertEqual(multiply(-10, 5), -50)
        self.assertEqual(divide(-10, 5), -2.0)

    def test_decimal_precision(self):
        """Verify calculations with floating-point values."""
        self.assertAlmostEqual(add(0.1, 0.2), 0.3)
        self.assertAlmostEqual(subtract(0.3, 0.1), 0.2)
        self.assertAlmostEqual(multiply(0.1, 0.2), 0.02)
        self.assertAlmostEqual(divide(0.3, 0.1), 3.0)


    def test_addition_multiple_cases(self):
        """Verify addition across multiple input scenarios."""

        test_cases = [
            (10, 5, 15),
            (0, 0, 0),
            (-10, 5, -5),
            (100, 200, 300),
            (1.5, 2.5, 4.0),
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                result = add(a, b)
                self.assertEqual(result, expected)

    def test_subtraction_multiple_cases(self):
        """Verify subtraction across multiple input scenarios."""

        test_cases = [
            (20, 10, 10),
            (0, 0, 0),
            (-10, 5, -15),
            (100, 200, -100),
            (5.5, 2.5, 3.0),
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                result = subtract(a, b)
                self.assertEqual(result, expected)

    def test_multiplication_multiple_cases(self):
        """Verify multiplication across multiple scenarios."""

        test_cases = [
            (10, 5, 50),
            (0, 100, 0),
            (-10, 5, -50),
            (-10, -5, 50),
            (2.5, 4, 10.0),
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                result = multiply(a, b)
                self.assertEqual(result, expected)

    def test_division_multiple_cases(self):
        """Verify division across multiple scenarios."""

        test_cases = [
            (20, 5, 4.0),
            (0, 10, 0.0),
            (-20, 5, -4.0),
            (-20, -5, 4.0),
            (7.5, 2.5, 3.0),
        ]

        for a, b, expected in test_cases:
            with self.subTest(a=a, b=b):
                result = divide(a, b)
                self.assertAlmostEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
