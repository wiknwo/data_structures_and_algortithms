# https://www.youtube.com/watch?v=Ph95IHmRp5M
"""
    Program to solve N-Queens problem using more advanced
    recursion and backtracking

    Given a value n, you need to create a chess grid of 
    size n x n and put n queens in it such that no queens 
    are in a mutual attacking position. A queen in a chess 
    board, can move to any direction horizontally, vertically, 
    and both ways diagonally.
"""
def solve_n_queens(n):
    """Function to solve N-Queens problem"""
    columns = set()
    positive_diagonals = set() # (r + c)
    negative_diagonals = set() # (r - c)
    solutions = [] # List to hold all possible N-Queen solutions
    chessboard = [(['.'] * n) for i in range(n)] # Creating n * n chesboard
    backtrack(0, n, chessboard, solutions, columns, positive_diagonals, negative_diagonals)
    return solutions

def backtrack(row, n, chessboard, solutions, columns, positive_diagonals, negative_diagonals):
    """Function to perform our backtracking in the N-Queens problem"""
    # Base case / stopping condition
    # We have found a valid N-Queens solution.
    # Row n means we have completed every single
    # row and we are out of bounds
    if row == n:
        # Add the current board to the solution set
        # but make a copy of the board because we will
        # use it in subsequent recursive calls.
        copy_of_chessboard = [''.join(r) for r in chessboard]
        solutions.append(copy_of_chessboard)
        return
    
    # We are going to try every column for the particular
    # row we are on to identify which position we can 
    # place the queen in.
    for column in range(n):
        # If eiter of these conditions are true then that means
        # we have to skip this position as the queen can be 
        # attacked if placed in this position
        if column in columns or (row + column) in positive_diagonals  or (row - column) in negative_diagonals:
            continue
        else:
            # Place queen in position
            columns.add(column)
            positive_diagonals.add(row + column)
            negative_diagonals.add(row - column)
            chessboard[row][column] = 'Q'

            # Inductive step: Do some work to shrink the problem space
            backtrack(row + 1, n, chessboard, solutions, columns, positive_diagonals, negative_diagonals)

            # Backtrack: Undo changes to check for more solutions
            columns.remove(column)
            positive_diagonals.remove(row + column)
            negative_diagonals.remove(row - column)
            chessboard[row][column] = '.'

if __name__ == '__main__':
    print(solve_n_queens(4))

