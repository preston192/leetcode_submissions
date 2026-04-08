# Last updated: 4/8/2026, 5:13:13 PM
class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            memo[i] = nums[i] + max(dp(i+2), dp(i+3))
            return memo[i]
        return max(dp(0), dp(1))