# Last updated: 4/8/2026, 5:13:41 PM
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        index = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[index] = nums[i]
                index += 1
        return index