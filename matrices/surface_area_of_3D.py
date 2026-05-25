from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        area = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] > 0:
                    area += 6 * grid[i][j]
                    area -= 2 * (grid[i][j] - 1)
                if i > 0:
                    area -= 2 * min(grid[i][j], grid[i-1][j])
                if j > 0:
                    area -= 2 * min(grid[i][j], grid[i][j-1])
        return area
