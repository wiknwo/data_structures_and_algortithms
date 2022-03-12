"""
    Program to sum all the natural numbers up to some input
    number demonstrating basic recursion
"""
def sum_natural_numbers(number):
    # Base case / stoppping condition
    if number == 0:
        return 0
    
    # Inductive step: Do some work to shrink the problem
    return number + sum_natural_numbers(number - 1)

if __name__ == '__main__':
    print(sum_natural_numbers(10))