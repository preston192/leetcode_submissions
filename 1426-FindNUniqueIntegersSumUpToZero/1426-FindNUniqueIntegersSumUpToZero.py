# Last updated: 4/8/2026, 5:11:19 PM
class Solution:
    def sumZero(self, n: int) -> List[int]:
        result = []
        for x in range(1, (n//2)+1):
            result.append(x)
            result.append(-x)

        if n%2 == 1:
            result.append(0)

        return result