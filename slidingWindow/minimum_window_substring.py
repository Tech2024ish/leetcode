from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        t_count = Counter(t)
        window_count = Counter()
        count = 0
        left = 0
        min_len = float('inf')
        start, end = 0, 0
        for right in range(len(s)):
            window_count[s[right]] += 1
            if window_count[s[right]] == t_count[s[right]]:
                count += 1
            while count == len(t_count):
                if (right - left + 1) < min_len:
                    min_len = right - left + 1
                    start, end = left, right
                window_count[s[left]] -= 1
                if window_count[s[left]] < t_count[s[left]]:
                    count -= 1
                left += 1
        return s[start:end+1] if min_len != float('inf') else ""
