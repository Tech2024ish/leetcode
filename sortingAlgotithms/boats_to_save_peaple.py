from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        size = len(people)
        left, right = 0, size-1
        counter = 0
        people.sort()
        while left <= right:
            tot = people[left] + people[right]
            if tot <= limit:
                counter += 1
                left += 1
                right -= 1
            else:
                counter += 1
                right -= 1
        return counter
