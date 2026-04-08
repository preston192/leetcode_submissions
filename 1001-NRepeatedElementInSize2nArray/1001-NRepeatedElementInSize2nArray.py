# Last updated: 4/8/2026, 5:26:18 PM
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        seen = set()

        for num in nums:
            if num in seen:
                return num
            else:
                seen.add(num)