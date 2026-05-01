from math import gcd
from collections import defaultdict
from typing import List


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_count = defaultdict(int)

        for w, h in rectangles:
            g = gcd(w, h)
            ratio_count[(w // g, h // g)] += 1
        return sum(count * (count - 1) // 2 for count in ratio_count.values())
