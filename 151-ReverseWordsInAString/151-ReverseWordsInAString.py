# Last updated: 4/8/2026, 5:13:18 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        string_split = s.split()
        return " ".join(string_split[::-1])