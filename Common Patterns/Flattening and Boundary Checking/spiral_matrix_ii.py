# https://leetcode.com/problems/spiral-matrix-ii/
class Solution:
    def generateMatrix(self, n):
        matrix = [[None] * n for i in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y = 0, 0
        current_direction = 0
        
        for number in range(1, n * n + 1):
            matrix[x][y] = number
            
            if number == n * n:
                continue
            
            while True:
                dx, dy = directions[current_direction]
                new_x, new_y = x + dx, y + dy
                
                if 0 <= new_x < n and 0 <= new_y < n and matrix[new_x][new_y] is None:
                    x, y = new_x, new_y
                    break
                    
                current_direction += 1
                current_direction %= 4
                
        return matrix