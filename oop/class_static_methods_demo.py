"""
Demonstration of class methods and static methods in Python.
Contains Calculator class with examples of both method types.
"""


class Calculator:
    """
    Calculator class demonstrating class methods and static methods.
    
    Class Attributes:
        calculation_type (str): Type of calculations performed
    """
    
    # Class attribute
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Args:
            a (int or float): First number
            b (int or float): Second number
            
        Returns:
            int or float: Sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        Demonstrates access to class attributes.
        
        Args:
            cls (class): Reference to the class
            a (int or float): First number
            b (int or float): Second number
            
        Returns:
            int or float: Product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b