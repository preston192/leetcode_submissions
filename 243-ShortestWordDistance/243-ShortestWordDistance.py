# Last updated: 4/8/2026, 5:15:02 PM
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        best = float("inf")
        n = len(wordsDict)
        last = ("" , -1)

        for i, word in enumerate(wordsDict):
            if word in (word1, word2):
                if last[0] and word != last[0]:
                    best = min(best, i - last[1])
                last = (word, i)

        return best
