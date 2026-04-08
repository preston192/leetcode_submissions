# Last updated: 4/8/2026, 5:12:11 PM
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts = {}
        best = 0
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for x in counts:
            if x + 1 in counts:
                best = max(best, counts[x] + counts[x + 1])

        return best