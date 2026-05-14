import re
from typing import List
from collections import Counter


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        words = re.sub(r'[^a-zA-Z]', ' ', paragraph).lower().split()
        freqs = Counter([word for word in words if word not in banned_set])
        return freqs.most_common(1)[0][0]
