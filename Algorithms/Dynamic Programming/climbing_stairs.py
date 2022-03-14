"""
Program to solve the climbing stairs problem using memoization: 
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct 
ways can you climb to the top?

There is way to solve this problem that uses O(1) space
do you know it?
"""
def climbing_stairs(n):
    # There is only one way to climb 0 steps 
    # and there is only one way to climb 1 step
    if n <= 1:
        return 1
    else:
        memo = [None] * (n + 1) # We are including the zero base case so we use n + 1
        memo[0], memo[1] = 1, 1 # There is only one way to climb 0 steps and there is only one way to climb 1 step
        # We are including n in our loop so we loop to n + 1 because of Python's loop construct
        for i in range(2, n + 1): 
            # Climbing the ith step we need to know how many steps 
            # we have taken from the previous step and the step before that
            memo[i] = memo[i - 1] + memo[i - 2] 
        return memo[n]

if __name__ == '__main__':
    print(climbing_stairs(2))