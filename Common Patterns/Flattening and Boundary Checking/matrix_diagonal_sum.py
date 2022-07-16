"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
# https://leetcode.com/problems/matrix-diagonal-sum/
class Solution:
    def diagonalSum(self, mat):
        # Checking for overlap of diagonals
        isoverlap = len(mat) % 2 == 1
        # Computing diagonals
        primary_diagonal = sum(mat[i][i] for i in range(len(mat)))
        secondary_diagonal = sum(mat[i][len(mat) - 1 - i] for i in range(len(mat)))
        # Accounting for overlapping element after computing diagonals
        matrix_center_index = len(mat) // 2
        secondary_diagonal -= mat[matrix_center_index][matrix_center_index] if isoverlap else 0
        # Return sum of diagonals
        return primary_diagonal + secondary_diagonal
    