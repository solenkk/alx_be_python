#!/usr/bin/env python3
"""
Demonstration of polymorphism and method overriding in Python.
Contains Shape base class and derived classes Rectangle and Circle.
"""

import math


class Shape:
    """Base class representing a geometric shape."""
    
    def area(self):
        """
        Calculate the area of the shape.
        
        This method should be overridden by derived classes.
        
        Raises:
            NotImplementedError: If the method is not overridden
        """
        raise NotImplementedError("Subclasses must override this method")


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""
    
    def __init__(self, length: float, width: float):
        """
        Initialize a Rectangle instance.
        
        Args:
            length (float): The length of the rectangle
            width (float): The width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self) -> float:
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: Area of rectangle (length × width)
        """
        return self.length * self.width


class Circle(Shape):
    """Circle class inheriting from Shape."""
    
    def __init__(self, radius: float):
        """
        Initialize a Circle instance.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self) -> float:
        """
        Calculate the area of the circle.
        
        Returns:
            float: Area of circle (π × radius²)
        """
        return math.pi * (self.radius ** 2)