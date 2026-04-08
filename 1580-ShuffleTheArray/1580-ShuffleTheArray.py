# Last updated: 4/8/2026, 5:08:45 PM
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = [x for pair in zip(nums[:n], nums[n:]) for x in pair]
        return result