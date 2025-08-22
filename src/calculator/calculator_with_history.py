"""
Simple calculator module for demonstrating basic unit testing concepts.

This module implements basic arithmetic operations and includes some
intentional design choices to demonstrate testing pitfalls and best practices.
"""

class CalculatorWithHistory:
    """
    A simple calculator class that performs basic arithmetic operations.
    
    This class is designed to demonstrate:
    - Basic unit testing
    - Edge case handling
    - Code coverage vs. test quality
    """
    
    def __init__(self):
        """Initialize the calculator."""
        self.history = []
    
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
        self.history.append(f"{a} + {b} = {result}")
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
        self.history.append(f"{a} - {b} = {result}")
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
        self.history.append(f"{a} * {b} = {result}")
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
        self.history.append(f"{a} / {b} = {result}")
        return result
    
    def get_history(self):
        """
        Get calculation history.
        
        Returns:
            list: List of calculation strings
        """
        return self.history.copy()
    
    def clear_history(self):
        """Clear calculation history."""
        self.history.clear()
    
    def power(self, base, exponent):
        """
        Calculate base raised to the power of exponent. 
        
        Args:
            base (float): Base number
            exponent (float): Exponent
            
        Returns:
            float: Result of base^exponent
        """
        output = self.__get_power_output(base, exponent)        
        self.history.append(f"{base} ^ {exponent} = {output}")
        return output
    
    def __get_power_output(self, base, exponent):
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