# Last updated: 4/8/2026, 5:08:20 PM
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        best_val = 0
        for k in range(2, n):
            maxPrefix = nums[0]
            for j in range(1, k):
                best_val = max(best_val, (maxPrefix - nums[j]) * nums[k])
                maxPrefix = max(maxPrefix, nums[j])
        return best_val