# Last updated: 4/8/2026, 5:12:28 PM
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aAeEiIoOuU")
        l = 0
        r = len(s)-1
        s_list = list(s)

        while l < r:
            if s_list[l] not in vowels:
                l += 1
                continue
            if s_list[r] not in vowels:
                r += -1
                continue
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r += -1
        
        return "".join(s_list)