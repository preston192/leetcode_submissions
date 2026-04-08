# Last updated: 4/8/2026, 5:13:09 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))