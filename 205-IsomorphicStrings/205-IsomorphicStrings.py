# Last updated: 4/8/2026, 5:13:10 PM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        alpha_map_s = {}
        alpha_map_t = {}

        if len(s) != len(t):
            return False

        for i, c in enumerate(s):
            if c in alpha_map_s:
                if t[i] != alpha_map_s[c]:
                    return False
            else:
                alpha_map_s[c] = t[i]
        

        for i, c in enumerate(t):
            if c in alpha_map_t:
                if s[i] != alpha_map_t[c]:
                    return False
            else:
                alpha_map_t[c] = s[i]

        return True