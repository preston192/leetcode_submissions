# Last updated: 4/8/2026, 5:13:11 PM
class Solution:
    def isHappy(self, n: int) -> bool:
        val = set()
        result = n
        while result != 1:
            val.add(result)
            temp = result
            result = 0
            while temp != 0:
                result += (temp % 10)**2
                temp //= 10
            if result in val:
                return False
        return True