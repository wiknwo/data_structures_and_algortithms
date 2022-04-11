# https://leetcode.com/problems/shift-2d-grid/
# https://stackoverflow.com/questions/2150108/efficient-way-to-rotate-a-list-in-python
from collections import deque
class Solution:
    def shiftGrid(self, grid, k):
        shifts = k % (len(grid) * len(grid[0]))
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                q.append(grid[i][j])
        q.rotate(shifts)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = q.popleft()
        return grid