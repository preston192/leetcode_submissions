# Last updated: 4/8/2026, 5:13:06 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, num in enumerate(nums):
            if num in seen and i-seen[num] <= k:
                return True
            seen[num] = i
        return False
        
        
            
            
        