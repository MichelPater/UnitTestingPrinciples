"""
Simple calculator module for demonstrating basic unit testing concepts.

This module implements basic arithmetic operations and includes some
intentional design choices to demonstrate testing pitfalls and best practices.
"""

class Calculator:
    """
    A simple calculator class that performs basic arithmetic operations.
    
    This class is designed to demonstrate:
    - Basic unit testing
    - Edge case handling
    - Code coverage vs. test quality
    """
    
    def add(self, a, b):
        """
        Add two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Sum of a and b
        """
        result = a + b
        return result
    
    def subtract(self, a, b):
        """
        Subtract second number from first number.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Difference of a and b
        """
        result = a - b
        return result
    
    def multiply(self, a, b):
        """
        Multiply two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: Product of a and b
        """
        result = a * b
        return result
    
    def divide(self, a, b):
        """
        Divide first number by second number.
        
        Args:
            a (float): Dividend
            b (float): Divisor
            
        Returns:
            float: Quotient of a and b
            
        Raises:
            ValueError: If divisor is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        
        result = a / b
        return result
    
    def power(self, base, exponent):
        """
        Calculate base raised to the power of exponent.
        
        Args:
            base (float): Base number
            exponent (float): Exponent
            
        Returns:
            float: Result of base^exponent
        """
        if exponent == 0:
            return 1
        elif exponent == 1:
            return base
        else:
            return base ** exponent