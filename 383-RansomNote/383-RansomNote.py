# Last updated: 4/8/2026, 5:12:24 PM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): 
            return False
            
        letters = collections.Counter(magazine)

        for c in ransomNote:
            if letters[c] <= 0:
                return False
            letters[c] += -1
        
        return True

