# Last updated: 4/8/2026, 5:12:17 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
        return [index + 1 for index, num in enumerate(nums) if num > 0]
