# Last updated: 4/8/2026, 5:12:23 PM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = collections.Counter(s)
        for c in s:
            if counter[c] == 1:
                return s.index(c)
        return -1


