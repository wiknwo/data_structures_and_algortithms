"""
Program to solve grid traveler problem
recursively. 

How many ways are there starting from 
the top left to reach the bottom right
while you can only move down or right.

The height of the tree we get when we 
analyze the recursion of function calls
is rows + columns - 1. Therefore the 
time complexity is 
2^(rows + columns - 1) ~ 2^(rows + columns)
because constants are ignored when calculating
Big O.  

https://stackoverflow.com/questions/68865667/why-does-grid-traveller-have-a-time-complexity-of-2nm

Time Complexity: O(2^(rows + columns))
Space Complexity: O(rows + columns)
"""
def grid_traveler(rows, columns):
    if rows == 1 and columns == 1:
        return 1
    if rows == 0 or columns == 0:
        return 0
    return grid_traveler(rows - 1, columns) + grid_traveler(rows, columns - 1)

if __name__ == '__main__':
    print(grid_traveler(1, 1)) # 1
    print(grid_traveler(2, 3)) # 3
    print(grid_traveler(3, 2)) # 3
    print(grid_traveler(3, 3)) # 6
    print(grid_traveler(18, 18)) # 2333606220