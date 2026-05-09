from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        start_map = sorted((interval[0], i)
                           for i, interval in enumerate(intervals))

        starts = [s[0] for s in start_map]
        result = []

        for interval in intervals:
            end = interval[1]

            low, high = 0, len(starts)
            while low < high:
                mid = (low + high) // 2
                if starts[mid] >= end:
                    high = mid
                else:
                    low = mid + 1

            if low < len(starts):
                result.append(start_map[low][1])
            else:
                result.append(-1)

        return result
