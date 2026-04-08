# Last updated: 4/8/2026, 5:14:59 PM
class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}

        def tribonacci(n):
            if n in memo:
                return memo[n]
            memo[n] = tribonacci(n-1) + tribonacci(n-2) + tribonacci(n-3)
            return memo[n]
        
        return tribonacci(n)