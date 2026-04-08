# Last updated: 4/8/2026, 5:08:14 PM
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        streak = 1

        if k*2 > len(nums):
            return False
        if k == 1:
            return True
            
        for i in range(len(nums) - k - 1):
            if nums[i] < nums[i+1] and nums[i+k] < nums[i+k+1]:
                streak += 1
                if streak == k:
                    return True
            else:
                streak = 1
        return False