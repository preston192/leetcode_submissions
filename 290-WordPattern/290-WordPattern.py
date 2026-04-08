# Last updated: 4/8/2026, 5:12:31 PM
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        p_to_s = {}
        s_to_p = {}

        if len(words) != len(pattern):
            return False

        for p, w in zip(pattern, words):
            if p in p_to_s and p_to_s[p] != w:
                return False
            if w in s_to_p and s_to_p[w] != p:
                return False
            p_to_s[p] = w
            s_to_p[w] = p
        
        return True

        

