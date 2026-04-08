# Last updated: 4/8/2026, 5:12:20 PM
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_s = Counter(s)
        length = 0
        odd = 0
        for char in count_s:
            if count_s[char] % 2 == 0:
                length += count_s[char]
            else:
                length += count_s[char] - 1
                odd += 1
        return length + int(bool(odd))