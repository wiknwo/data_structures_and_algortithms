"""
    Program to determine if a string is a palindrome by 
    demonstrating basic recursion
"""
def is_palindrome(s):
    # Base case / stopping condition
    if len(s) == 0 or len(s) == 1:
        return True

    # Inductive step: Do some work to shrink the problem space
    if s[0] == s[len(s) - 1]:
        return is_palindrome(s[1:len(s) - 1])
    
    # Additional base case to handle non-palindromes
    return False

if __name__ == '__main__':
    print(is_palindrome('racecar'))