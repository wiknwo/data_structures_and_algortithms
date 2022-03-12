"""
    Program to reverse a string demonstrating basic recursion
"""
def string_reversal(s):
    # Base case:
    if s == '':
        return ''
    
    # Inductive step:
    return string_reversal(s[1:]) + s[0]

if __name__ == '__main__':
    print(string_reversal('hello'))