"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        if len(grid) < 1:
            return 0
        for r in range(0, len(grid)):
            for c in range(0, len(grid[0])):
                if grid[r][c] == '1':
                    self.traverse(r,c,grid)
                    res += 1
        return res
                    
    def traverse(self, r, c, grid):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return
        if grid[r][c] == '1':
            grid[r][c] = 0
            
            self.traverse(r-1, c, grid)
            self.traverse(r+1, c, grid)
            self.traverse(r, c-1, grid)
            self.traverse(r, c+1, grid)
            
            
        
