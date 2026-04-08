# Last updated: 4/8/2026, 5:08:15 PM
from collections import Counter
class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        result = []
        for i in range(n-k+1):
            count = Counter(nums[i:i+k])
            freq = sorted(count.items(), key=lambda x: (-x[1], - x[0]))
            x_sum = sum(key * value for key, value in freq[:x])
            result.append(x_sum)
        return result