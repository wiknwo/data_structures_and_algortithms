"""
    Program to solve a 9 x 9 Sudoku grid given it has a unique solution.
    This is an example of a recursion and backtracking algorithm that is
    a bit more advanced.
"""
def isValid(board, row, column):
    """Function to check if state is valid"""
    for i in range(len(board)):
        if i != row and board[i][column] == board[row][column]:
            return False
    for j in range(len(board[0])):
        if j != column and board[row][j] == board[row][column]:
            return False
    i = 3 * (row // 3)
    while i < 3 * (row // 3 + 1):
        j = 3 * (column // 3)
        while j < 3 * (column // 3 + 1):
            if (i != row or j != column) and board[i][j] == board[row][column]:
                return False
            j += 1
        i += 1
    return True

def solver(board):
    """Function to solve Sudoku and perform backtracking"""
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.':
                for number in range(1, 10):
                    board[i][j] = str(number)
                    if isValid(board, i, j) and solver(board):
                        return True
                    board[i][j] = '.'
                return False
    return True

def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """
    solver(board)

if __name__ == '__main__':
    grid = [ ["5","3",".",".","7",".",".",".","."],
             ["6",".",".","1","9","5",".",".","."],
             [".","9","8",".",".",".",".","6","."],
             ["8",".",".",".","6",".",".",".","3"],
             ["4",".",".","8",".","3",".",".","1"],
             ["7",".",".",".","2",".",".",".","6"],
             [".","6",".",".",".",".","2","8","."],
             [".",".",".","4","1","9",".",".","5"],
             [".",".",".",".","8",".",".","7","9"] ]

    solveSudoku(grid)
    print('\n'.join(str(row) for row in grid))