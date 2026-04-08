# Last updated: 4/8/2026, 5:12:15 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, 0
        best = 0

        while l < n and r < n:
            while l < n and nums[l] == 0:
                l += 1
            r = l
            while r < n and nums[r] == 1:
                r += 1
            best = max(best, r - l)
            l = r
        
        return best