from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp

        for row in matrix:
            left, right = 0, len(row)-1
            while left < right:
                temp = row[left]
                row[left] = row[right]
                row[right] = temp
                left += 1
                right -= 1
