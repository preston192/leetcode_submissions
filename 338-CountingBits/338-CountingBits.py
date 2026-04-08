# Last updated: 4/8/2026, 5:12:29 PM
class Solution:
    def countBits(self, n: int) -> List[int]:
        numbers = [str(bin(x))[2:] for x in range(0, n + 1)]
        result = [0] * (n + 1)
        for index, binary in enumerate(numbers):
            count = collections.Counter(binary).get("1",0)
            result[index] = count
        return result