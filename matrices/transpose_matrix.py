from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])

        transMat = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                transMat[i][j] = matrix[j][i]
        return transMat
