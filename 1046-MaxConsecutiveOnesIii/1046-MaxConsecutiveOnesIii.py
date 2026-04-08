# Last updated: 4/8/2026, 5:11:58 PM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        zeros = 0
        best = 0

        for r, x in enumerate(nums):
            if x == 0:
                zeros += 1
            while zeros > k:
                if nums[l] == 0:
                    zeros += -1
                l += 1
            best = max(best, r-l+1)
        
        return best