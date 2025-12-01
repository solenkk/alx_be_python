import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test suite for the SimpleCalculator class."""

    def setUp(self):
        """Set up a fresh SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various scenarios."""
        # Test basic addition
        self.assertEqual(self.calc.add(2, 3), 5)
        
        # Test addition with negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        
        # Test addition with two negative numbers
        self.assertEqual(self.calc.add(-5, -3), -8)
        
        # Test addition with zero
        self.assertEqual(self.calc.add(0, 10), 10)
        self.assertEqual(self.calc.add(10, 0), 10)
        
        # Test addition with decimal numbers
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0)
        
        # Test addition with large numbers
        self.assertEqual(self.calc.add(1000, 2000), 3000)

    def test_subtraction(self):
        """Test the subtraction method with various scenarios."""
        # Test basic subtraction
        self.assertEqual(self.calc.subtract(5, 3), 2)
        
        # Test subtraction with negative result
        self.assertEqual(self.calc.subtract(3, 5), -2)
        
        # Test subtraction with negative numbers
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        
        # Test subtraction with zero
        self.assertEqual(self.calc.subtract(10, 0), 10)
        self.assertEqual(self.calc.subtract(0, 10), -10)
        
        # Test subtraction with decimal numbers
        self.assertEqual(self.calc.subtract(5.5, 2.5), 3.0)
        
        # Test subtraction with large numbers
        self.assertEqual(self.calc.subtract(5000, 2000), 3000)

    def test_multiplication(self):
        """Test the multiplication method with various scenarios."""
        # Test basic multiplication
        self.assertEqual(self.calc.multiply(2, 3), 6)
        
        # Test multiplication with negative numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)
        self.assertEqual(self.calc.multiply(-2, -3), 6)
        
        # Test multiplication with zero
        self.assertEqual(self.calc.multiply(0, 10), 0)
        self.assertEqual(self.calc.multiply(10, 0), 0)
        
        # Test multiplication with one
        self.assertEqual(self.calc.multiply(1, 10), 10)
        self.assertEqual(self.calc.multiply(10, 1), 10)
        
        # Test multiplication with decimal numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        
        # Test multiplication with large numbers
        self.assertEqual(self.calc.multiply(100, 50), 5000)

    def test_division(self):
        """Test the division method with various scenarios."""
        # Test basic division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        
        # Test division with decimal result
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        
        # Test division with negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        
        # Test division with zero numerator
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        
        # Test division resulting in whole number
        self.assertEqual(self.calc.divide(9, 3), 3.0)
        
        # Test division with decimal numbers
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_division_by_zero(self):
        """Test division by zero returns None as specified."""
        # Test division by zero returns None
        self.assertIsNone(self.calc.divide(10, 0))
        
        # Test division by zero with negative numerator
        self.assertIsNone(self.calc.divide(-10, 0))
        
        # Test division by zero with zero numerator
        self.assertIsNone(self.calc.divide(0, 0))

if __name__ == '__main__':
    unittest.main()
