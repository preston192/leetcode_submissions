# Last updated: 4/8/2026, 5:14:25 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}
        for i, num in enumerate(nums):
            if num in complement:
                return [i, complement[num]]
            else: 
                complement[target - num] = i
        