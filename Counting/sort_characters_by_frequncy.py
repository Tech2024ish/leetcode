from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        result = []
        for ch, val in sorted(freq.items(), key=lambda x: -x[1]):
            for _ in range(val):
                result.append(ch)
        return "".join(result)
