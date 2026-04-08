# Last updated: 4/8/2026, 5:12:22 PM
from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count_s = Counter(s)    
        for char in t:
            if char not in count_s or count_s[char] == 0:
                return char
            else:
                count_s[char] += -1