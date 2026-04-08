# Last updated: 4/8/2026, 5:12:33 PM
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            result = 0
            while num > 0:
                result += num % 10
                num //= 10
            num = result
        return num