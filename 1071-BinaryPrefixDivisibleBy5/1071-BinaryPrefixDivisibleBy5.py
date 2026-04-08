# Last updated: 4/8/2026, 5:11:57 PM
class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        result = [False] * len(nums)
        curr = 0

        for i, num in enumerate(nums):
            curr = (curr * 2 + num) % 5
            result[i] = curr == 0
        
        return result