class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        # use merge sort
        def merge_sort(new_nums):
            if len(new_nums) < 2:
                return new_nums

            left, right = split(new_nums)
            left = merge_sort(left)
            right = merge_sort(right)

            return merge(left, right)

        # breakdown list into two sublists
        def split(new_nums):

            mid = len(new_nums)//2
            left = new_nums[:mid]
            right = new_nums[mid:]

            return left, right

        # combine two lists
        def merge(left, right):

            left_len, right_len = len(left), len(right)
            merged_nums = [0] * (left_len + right_len)
            i, j = 0, 0
            k = 0

            while i < left_len and j < right_len:

                if left[i] <= right[j]:
                    merged_nums[k] = left[i]
                    i += 1
                else:
                    merged_nums[k] = right[j]
                    j += 1
                k += 1
            while i < left_len:
                merged_nums[k] = left[i]
                i += 1
                k += 1
            while j < right_len:
                merged_nums[k] = right[j]
                j += 1
                k += 1

            return merged_nums

        return merge_sort(nums)
