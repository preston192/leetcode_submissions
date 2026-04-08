# Last updated: 4/8/2026, 5:12:06 PM
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {len(cost): 0, len(cost)+1: 0}
        def dp(i):
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(dp(i+1), dp(i+2))
            return memo[i]
        return min(dp(0), dp(1))