# Last updated: 4/8/2026, 5:13:32 PM
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return int(math.factorial(m+n-2) / (math.factorial(m-1) * math.factorial(n-1)))