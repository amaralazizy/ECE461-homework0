
"""
This is a dummy Python file created for testing purposes. 
It contains basic mathematical operations such as addition, 
subtraction, multiplication, and division. The primary objective 
of this file is to serve as a placeholder for developing and 
testing a Python project. The functions included in this file 
are simple yet fundamental, providing a straightforward 
framework for conducting initial tests and ensuring that the 
testing environment is correctly set up. This dummy file is 
also useful for practicing version control, debugging, and 
collaboration among team members in a development setting. 
It is not intended for production use or complex calculations.
dummy change "Amar AlAzizy"
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
def modulus(a,b):
    return a%b

if __name__ == "__main__":
    print("Addition of 10 and 5:", add(10, 5))
    print("Subtraction of 10 and 5:", subtract(10, 5))
    print("Multiplication of 10 and 5:", multiply(10, 5))
    print("Division of 10 by 5:", divide(10, 5))
