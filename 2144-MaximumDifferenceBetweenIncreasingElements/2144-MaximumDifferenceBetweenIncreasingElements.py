# Last updated: 4/8/2026, 5:08:35 PM
class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        n = len(nums)
        best, premin = -1, nums[0]

        for j in range(1, n):
            if nums[j] > premin:
                best = max(best, nums[j] - premin)
            else:
                premin = nums[j]

        return best