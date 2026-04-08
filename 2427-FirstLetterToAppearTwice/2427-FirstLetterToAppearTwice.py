# Last updated: 4/8/2026, 5:08:28 PM
class Solution:
    def repeatedCharacter(self, s: str) -> str:
        freq = {}
        for c in s:
            if c not in freq:
                freq[c] = 1
            else: 
                return c