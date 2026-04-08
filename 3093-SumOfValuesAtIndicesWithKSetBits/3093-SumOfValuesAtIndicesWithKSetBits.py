# Last updated: 4/8/2026, 5:08:21 PM
class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        return sum(num for i, num in enumerate(nums) if bin(i).count("1") == k)
        