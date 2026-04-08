# Last updated: 4/8/2026, 5:12:22 PM
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0

        if not s:
            return True
        
        for c in t:
            if s[count] == c:
                count += 1
            if count == len(s):
                return True
        return False