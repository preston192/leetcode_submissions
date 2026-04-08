# Last updated: 4/8/2026, 5:08:31 PM
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums.sort()
        running = 0
        for i, num in enumerate(nums):
            if i % 2 == 0:
                running += num
            else:
                running += -num
        return running == 0