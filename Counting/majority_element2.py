from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        return [key for key, val in freq if val > len(nums)/3]
