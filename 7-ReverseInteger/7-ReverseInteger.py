# Last updated: 4/8/2026, 5:14:19 PM
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x *= sign

        reversed_int = int(str(x)[::-1]) * sign

        if -2 ** 31 <= reversed_int <= 2 ** 31 -1:
            return reversed_int
        return 0
        
