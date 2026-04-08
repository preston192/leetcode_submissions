# Last updated: 4/8/2026, 5:13:14 PM
class Solution:
    def reverseBits(self, n: int) -> int:
        ret, power = 0, 31
        
        while n:
            ret += (n & 1) << power
            n = n >> 1
            power += -1
        
        return ret