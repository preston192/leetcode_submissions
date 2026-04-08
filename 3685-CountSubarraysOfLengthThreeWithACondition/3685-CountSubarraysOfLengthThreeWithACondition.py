# Last updated: 4/8/2026, 5:08:12 PM
class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0

        for i in range(2, len(nums)):
            if (nums[i-2] + nums[i]) * 2 == nums[i-1]:
                count += 1

        return count 