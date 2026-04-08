# Last updated: 4/8/2026, 5:08:09 PM
class Solution:
    def maxDifference(self, s: str) -> int:
        freq = Counter(s)
        odd_max = max(x for x in freq.values() if x % 2 == 1)
        even_min = min(x for x in freq.values() if x % 2 == 0)
        
        return odd_max - even_min