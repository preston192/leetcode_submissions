# Last updated: 4/8/2026, 5:08:13 PM
class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
        return count