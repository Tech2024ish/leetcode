from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums)-2):
            left, right = i + 1, len(nums)-1

            while left < right:
                tot = nums[i] + nums[left] + nums[right]

                if abs(tot - target) < abs(closest - target):
                    closest = tot

                if tot < target:
                    left += 1
                elif tot > target:
                    right -= 1
                else:
                    return tot
        return closest
