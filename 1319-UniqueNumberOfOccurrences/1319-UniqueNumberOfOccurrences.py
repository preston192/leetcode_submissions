# Last updated: 4/8/2026, 5:15:01 PM
from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq = Counter(arr)
        counts = set(freq.values())
        return len(counts) == len(freq.keys())
            