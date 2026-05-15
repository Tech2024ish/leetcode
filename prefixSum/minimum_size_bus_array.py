from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        size = len(nums)
        left = 0
        tot = 0
        min_window_size = float('inf')
        for right in range(size):
            tot += nums[right]
            while tot >= target:
                curr_window_size = right - left + 1
                min_window_size = min(min_window_size, curr_window_size)
                tot -= nums[left]
                left += 1
        return 0 if min_window_size == float('inf') else min_window_size
