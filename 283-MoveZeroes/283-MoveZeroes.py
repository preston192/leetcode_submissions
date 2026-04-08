# Last updated: 4/8/2026, 5:12:32 PM
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums.sort(key=lambda x: x == 0)
        