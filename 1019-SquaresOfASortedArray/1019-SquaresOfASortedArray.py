# Last updated: 4/8/2026, 5:11:59 PM
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            result.append(nums[i] ** 2)
        return sorted(result)
        