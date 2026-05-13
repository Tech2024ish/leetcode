from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_count = Counter(words)
        return sorted(words_count, key=lambda x: (-words_count[x], x))[:k]
