# Last updated: 4/8/2026, 5:13:30 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        a, b = 1, 2
        for _ in range(3, n+1):
            a, b = b, a + b

        return b