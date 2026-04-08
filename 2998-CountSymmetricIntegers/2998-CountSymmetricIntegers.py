# Last updated: 4/8/2026, 5:08:25 PM
class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for num in range(low, high+1):
            n = len(str(num))
            if n%2!=0:
                continue
            num_list = [int(x) for x in list(str(num))]
            if sum(num_list[:(n//2)]) == sum(num_list[n//2:]):
                count += 1
        return count