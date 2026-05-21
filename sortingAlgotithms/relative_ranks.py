from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_indices = sorted(
            range(len(score)), key=lambda i: score[i], reverse=True)

        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        result = [""] * len(score)

        for rank, idx in enumerate(sorted_indices):
            result[idx] = medals[rank] if rank < 3 else str(rank + 1)

        return result
