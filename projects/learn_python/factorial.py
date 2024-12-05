"""
    Calculates the factorial of a number:
    
    if you call factorial(5), the function will calculate 5! which is 5 * 4 * 3 * 2 * 1, resulting in 120.
"""
def factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial
