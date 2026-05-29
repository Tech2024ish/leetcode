class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        first = 0
        unique = set()
        max_window_size = 0
        for last in range(size):
            while s[last] in unique:
                unique.remove(s[first])
                first += 1
            unique.add(s[last])
            max_window_size = max(max_window_size, last-first+1)
        return max_window_size
