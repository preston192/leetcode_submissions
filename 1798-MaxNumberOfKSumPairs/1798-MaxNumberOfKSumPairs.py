# Last updated: 4/8/2026, 5:08:41 PM
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        seen = {}
        count = 0
        for num in nums:
            complement = k-num
            if seen.get(complement,0) > 0:
                count += 1
                seen[complement] += -1
            else: 
                seen[num] = seen.get(num, 0) + 1
        return count