# Last updated: 4/8/2026, 5:08:33 PM
class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        reversed1 = int(str(num)[::-1])
        reversed2 = int(str(reversed1)[::-1])
        return reversed2 == num