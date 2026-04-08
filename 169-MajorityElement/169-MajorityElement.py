# Last updated: 4/8/2026, 5:13:15 PM
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        size = len(nums)
        for num in counts:
            if counts[num] > size // 2:
                return num