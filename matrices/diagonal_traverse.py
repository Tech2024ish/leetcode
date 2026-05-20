from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows, cols = len(mat), len(mat[0])
        diagonals = [[] for _ in range(rows+cols-1)]

        for r in range(rows):
            for c in range(cols):
                diagonals[r+c].append(mat[r][c])

        result = []
        for i in range(len(diagonals)):
            if i % 2 == 1:
                result.extend(diagonals[i])
            else:
                result.extend(diagonals[i][::-1])
        return result
