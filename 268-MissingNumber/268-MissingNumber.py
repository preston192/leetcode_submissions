# Last updated: 4/8/2026, 5:15:02 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n + 1) / 2
        return int(total - sum(nums)) 