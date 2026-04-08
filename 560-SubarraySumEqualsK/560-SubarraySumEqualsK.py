# Last updated: 4/8/2026, 5:12:12 PM
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = 0
        seen = {}
        seen[0] = 1
        count = 0

        for num in nums:
            prefix += num
            if prefix-k in seen:
                count += seen[prefix-k]
            else:
                seen[prefix-k] = 0
            if prefix in seen:
                seen[prefix] += 1
            else:
                seen[prefix] = 1
        
        return count