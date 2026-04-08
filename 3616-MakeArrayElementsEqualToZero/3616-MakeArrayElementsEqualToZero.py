# Last updated: 4/8/2026, 5:08:14 PM
class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + num)
        
        for i in range(n):
            if nums[i] == 0:
                if prefix[i] * 2 == prefix[-1]:
                    count += 2
                elif abs(prefix[i] * 2 - prefix[-1]) == 1:
                    count += 1
        
        return count

