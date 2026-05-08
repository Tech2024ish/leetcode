from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dpro = [[0] * (cols + 1) for _ in range(rows + 1)]
        max_side = 0

        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                if matrix[r-1][c-1] == '1':
                    dpro[r][c] = min(dpro[r-1][c], dpro[r]
                                     [c-1], dpro[r-1][c-1]) + 1
                    max_side = max(max_side, dpro[r][c])
        return max_side * max_side
