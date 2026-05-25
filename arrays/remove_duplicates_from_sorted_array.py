from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read = 0
        write = 1
        seen = nums[0]
        n = len(nums)
        while read < n:
            if nums[read] != seen:
                seen = nums[read]
                nums[write] = nums[read]
                write += 1
            read += 1
        return write
