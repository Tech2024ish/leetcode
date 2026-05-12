from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        fre = Counter(nums)
        return [k for k, val in sorted(fre.items(), key=lambda x: (-x[1], x[0]))[:k]]
