"""
Program to compute nth fibonacci number using
dynamic programming (memoization).
"""
def fibonacci(n, memo = {}): 
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        return n
    else:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
        return memo[n]

if __name__ == '__main__':
    print(fibonacci(50))