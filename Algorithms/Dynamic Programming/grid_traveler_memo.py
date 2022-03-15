"""
Program to solve grid traveler problem
using memoization. 

How many ways are there starting from 
the top left to reach the bottom right
while you can only move down or right.

Time Complexity: O(rows * columns)
Space Complexity: O(rows + columns)
"""
def grid_traveler(rows, columns, memo = {}):
    """
    We exploit the fact that grid_traveler(a, b) = grid_traveler(b, a)
    """
    key = str(rows) + ',' + str(columns)
    # Base cases / stopping conditions
    if key in memo:
        return memo[key]
    if rows == 1 and columns == 1:
        return 1
    if rows == 0 or columns == 0:
        return 0
    # Inductive step: Do some work to shrink the problem space
    memo[key] = grid_traveler(rows - 1, columns, memo) + grid_traveler(rows, columns - 1, memo)
    return memo[key]

if __name__ == '__main__':
    print(grid_traveler(1, 1)) # 1
    print(grid_traveler(2, 3)) # 3
    print(grid_traveler(3, 2)) # 3
    print(grid_traveler(3, 3)) # 6
    print(grid_traveler(18, 18)) # 2333606220