# Last updated: 4/8/2026, 5:13:07 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0