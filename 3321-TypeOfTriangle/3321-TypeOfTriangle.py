# Last updated: 4/8/2026, 5:08:18 PM
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        nums_s = set(nums)
        if max(nums) >= sum(nums) - max(nums):
            return "none"
        if len(nums_s) == 1:
            return "equilateral"
        elif len(nums_s) == 2:
            return "isosceles"
        else:
            return "scalene"