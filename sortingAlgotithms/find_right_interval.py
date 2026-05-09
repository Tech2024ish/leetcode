from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_map = sorted((interval[0], i)
                           for i, interval in enumerate(intervals))

        starts = [s[0] for s in start_map]
        result = []

        for interval in intervals:
            end = interval[1]

            lo, hi = 0, len(starts)
            while lo < hi:
                mid = (lo + hi) // 2
                if starts[mid] >= end:
                    hi = mid
                else:
                    lo = mid + 1

            if lo < len(starts):
                result.append(start_map[lo][1])
            else:
                result.append(-1)

        return result
