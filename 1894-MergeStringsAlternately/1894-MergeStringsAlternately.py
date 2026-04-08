# Last updated: 4/8/2026, 5:08:39 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        n = min(len(word1), len(word2))

        for i in range(n):
            result.append(word1[i])
            result.append(word2[i])

        if n < len(word1):
            result.append(word1[n:])
        elif n < len(word2):
            result.append(word2[n:])

        return "".join(result)