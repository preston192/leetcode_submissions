# Last updated: 4/8/2026, 5:08:11 PM
class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        best = -float("inf")
        curr = 0
        
        for i in range(len(nums)-1):
            curr = abs(nums[i] - nums[i+1])
            best = max(best, curr)
        
        best = max(best, abs(nums[0]-nums[-1]))
        return best