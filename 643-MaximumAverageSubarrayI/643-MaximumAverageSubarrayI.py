# Last updated: 4/8/2026, 5:12:10 PM
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        best = sum(nums[0:k])
        current_sum = sum(nums[0:k])

        for i in range(k, len(nums)):
            current_sum = current_sum - nums[i - k] + nums[i]
            best = max(best, current_sum)
            
        return best/k