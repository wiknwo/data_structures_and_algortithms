"""
    Program to compute the nth Fibonacci number demonstrating
    basic recursion. We will revisit this problem in dynamic
    programming (memoization) to make an optimal solution.
"""
def fibonacci(number):
    # Base case / stopping condition
    if number == 0 or number == 1:
        return number
    
    # Inductive step: Do some work to shrink the problem space
    return fibonacci(number - 1) + fibonacci(number - 2)

if __name__ == '__main__':
    print(fibonacci(11))