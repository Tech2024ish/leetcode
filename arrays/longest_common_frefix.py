from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        sorted_strs = sorted(strs)
        left = sorted_strs[0]
        right = sorted_strs[-1]
        i = 0
        answer = ""
        while i < min(len(left), len(right)):
            if left[i] == right[i]:
                answer += left[i]
            else:
                break
            i += 1
        return answer
