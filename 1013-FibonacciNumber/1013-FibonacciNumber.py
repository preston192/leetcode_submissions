# Last updated: 4/8/2026, 5:12:00 PM
class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        def dp(n):
            if n in memo:
                return memo[n]
            if n <= 1:
                return n
            memo[n] = dp(n-1) + dp(n-2)
            return memo[n]
        return dp(n)