class Solution:
    def rotate(self, grid):
        """
        Do not return anything, modify matrix in-place instead.
        """
        # transpose
        for i in range(len(grid)):
            for j in range(i, len(grid)):
                grid[i][j], grid[j][i] = grid[j][i], grid[i][j]
        # rotate
        for i in range(len(grid)):
            for j in range(len(grid)//2):
                grid[i][j], grid[i][-1*(j+1)] = grid[i][-1*(j+1)], grid[i][j]