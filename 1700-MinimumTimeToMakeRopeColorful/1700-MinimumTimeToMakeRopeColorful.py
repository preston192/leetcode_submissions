# Last updated: 4/8/2026, 5:08:42 PM
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        keep = 0
        prev = ""

        for c, t in zip(colors, neededTime):
            if c == prev:
                total += min(keep, t)
                keep = max(keep, t)
            else:
                keep = t
                prev = c

        return total