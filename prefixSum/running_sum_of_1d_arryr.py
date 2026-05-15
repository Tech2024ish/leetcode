from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        prev_sum = 0
        for i in range(len(nums)):
            prev_sum += nums[i]
            result[i] = prev_sum
        return result
