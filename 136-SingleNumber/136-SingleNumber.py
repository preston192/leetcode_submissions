# Last updated: 4/8/2026, 5:13:19 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)