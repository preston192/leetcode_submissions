# Last updated: 4/8/2026, 5:12:16 PM
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        freq = Counter(s)
        
        buckets = {}
        for c, count in freq.items():
            buckets.setdefault(count, []).append(c)
        
        result = []
        for count in sorted(buckets.keys(), reverse=True):
            for c in buckets[count]:
                result.append(c * count)
                
        return ''.join(result)
