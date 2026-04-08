# Last updated: 4/8/2026, 5:12:19 PM
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums_s = set(nums)
        if len(nums_s) < 3:
            return max(nums_s)
        
        nums.sort(reverse=True)
        count = 1
        third_max = -float("inf")
        for i in range(len(nums)):
            if nums[i] != nums[i+1]:
                count += 1
            if count == 3:
                return nums[i+1]