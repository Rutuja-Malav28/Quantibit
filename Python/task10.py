# implement unit tests for factorial calculation. 
# Input: factorial(5) 
# Output: 120 
# Test Case Output: 
# Test Passed for input 5 
# Test Passed for input 0 

def factorial(n):
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        fact = 1
        for i in range(2, n + 1):
            fact *= i  
        return fact
    else:
        raise ValueError("Input must be a non-negative integer.")


import unittest

class TestFactorial(unittest.TestCase):
    
    def test_factorial_5(self):
        self.assertEqual(factorial(5), 120) 
        print("Test Passed for input 5")
    
    def test_factorial_0(self):
        self.assertEqual(factorial(0), 1) 
        print("Test Passed for input 0")

if __name__ == '__main__':
    unittest.main()
