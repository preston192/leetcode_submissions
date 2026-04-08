# Last updated: 4/8/2026, 5:08:47 PM
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        s_l = list(s)
        best = 0
        curr = 0
        vowel = set("aeiou")
        r = 0
        l = 0

        while r < k:
            if s_l[r] in vowel:
                curr += 1
            r += 1
        best = curr

        while r < len(s):
            if best == k:
                return k
            if s_l[l] in vowel:
                curr += -1
            if s_l[r] in vowel:
                curr += 1
            best = max(best, curr)
            l += 1
            r += 1
            
        return best