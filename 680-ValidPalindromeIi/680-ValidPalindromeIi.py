# Last updated: 4/8/2026, 5:12:09 PM
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_pal(st):
            return st == st[::-1]
        
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return is_pal(s[l + 1: r + 1]) or is_pal(s[l: r])
            l += 1
            r += -1
        
        return True