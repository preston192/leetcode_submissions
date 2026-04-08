# Last updated: 4/8/2026, 5:08:11 PM
class Solution:
    def maxSum(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        total = 0
        largest = -float("inf")
        deleted = 0
        seen = set()

        for num in nums:
            largest = max(largest, num)
            if num < 0:
                deleted += 1
                continue
            if num in seen:
                deleted += 1
                continue
            else:
                seen.add(num)
            total += num
        
        return total if deleted < n else largest