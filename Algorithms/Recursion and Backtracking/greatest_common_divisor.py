"""
    Program to compute the euclidean algorithm also known as 
    the greates common divisor or GCD demonstrating basic
    recursion. It is also an example of a decrease-and-conquer
    algorithm.

    GCD of two numbers is the largest number that divides both of them. 
    A simple way to find GCD is to factorize both numbers and multiply 
    common prime factors.
"""
def gcd(a, b):
    # Base case / stopping condition
    if a == 0:
        return b
    
    # Inductive step: Do some work to shrink the problem space
    return gcd(b % a, a)

if __name__ == '__main__':
    print(gcd(100, 15))