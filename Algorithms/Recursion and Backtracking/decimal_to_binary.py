"""
    Program to convert decimal to binary demonstrating
    basic recursion
"""
def decimal_to_binary(decimal):
    # Base case / stopping condition
    if decimal == 0:
        return 0
    else:
        # Inductive step: Do some work to shrink the problem space
        return (decimal % 2 + 10 * decimal_to_binary(int(decimal // 2)))

if __name__ == '__main__':
    print(decimal_to_binary(4))