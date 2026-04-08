# Last updated: 4/8/2026, 5:11:16 PM
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        prefix.sort()
        if prefix[0] < 0:
            return -prefix[0] + 1
        else:
            return 1
        