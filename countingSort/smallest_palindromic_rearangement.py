class Solution:
    def smallestPalindrome(self, s: str) -> str:

        if len(s) < 2:
            return s

        freq = dict()

        for c in s:
            freq[c] = freq.get(c, 0) + 1

        left_half = []
        middle = ""
        for c in sorted(freq.keys()):
            pairs = freq[c] // 2
            left_half.extend([c] * pairs)

            if freq[c] % 2 == 1:
                middle = c

        right_half = left_half[::-1]
        return "".join(left_half) + middle + "".join(right_half)
