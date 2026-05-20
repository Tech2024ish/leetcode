from typing import List


class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows, cols = len(img), len(img[0])

        result = [[0]*cols for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                total, counter = 0, 0
                for i in range(r-1, r+2):
                    for j in range(c-1, c+2):
                        if i < 0 or i >= rows or j < 0 or j >= cols:
                            continue
                        total += img[i][j]
                        counter += 1
                result[r][c] = total//counter
        return result
