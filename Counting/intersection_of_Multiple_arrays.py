from collections import Counter
from typing import List


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = Counter()
        for row in nums:
            for num in row:
                count[num] += 1
        n = len(nums)
        return sorted(num for num, freq in count.items() if freq == n)
