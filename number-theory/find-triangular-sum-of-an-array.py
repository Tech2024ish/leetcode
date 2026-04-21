from typing import List


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        coeff = 1
        for i in range(n):
            res = (res + coeff * nums[i]) % 10
            coeff = coeff * (n - 1 - i) // (i + 1)
        return res % 10
