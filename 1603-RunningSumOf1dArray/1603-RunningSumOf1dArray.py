# Last updated: 4/8/2026, 5:08:45 PM
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [nums[0]]
        for i in range(1, len(nums)):
            result.append(result[-1] + nums[i])
        return result