# Last updated: 4/8/2026, 5:16:44 PM
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        complement = {}
4        
5        for i, num in enumerate(nums):
6            if num in complement:
7                return [i, complement[num]]
8            else: 
9                complement[target - num] = i
10        