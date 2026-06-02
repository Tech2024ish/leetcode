from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:

        offset = 10000
        count = [0] * 20001

        for num in nums:
            count[num + offset] += 1

        tot = 0
        pair_first = True

        for i in range(20001):

            while count[i] > 0:
                if pair_first:
                    tot += i - offset
                pair_first = not pair_first
                count[i] -= 1
        return tot


nums = [1, 4, 3, 2]
s = Solution()
print(s.arrayPairSum(nums))
