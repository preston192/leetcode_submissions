# Last updated: 4/8/2026, 5:12:07 PM
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = []
        right = []
        curr = 0
        n = len(nums)

        if len(nums) == 1:
            return 0
            
        for num in nums:
            curr += num
            left.append(curr)
        
        curr = 0
        for num in reversed(nums):
            curr += num
            right.append(curr)
        right.reverse()

        for i in range(n):
            if i == 0:
                if right[1] == 0:
                    return i
                continue
            if i == n-1:
                if left[-2] == 0:
                    return i
                continue
            if left[i-1] == right[i+1]:
                return i

        return -1