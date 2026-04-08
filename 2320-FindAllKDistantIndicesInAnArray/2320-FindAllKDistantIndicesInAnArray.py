# Last updated: 4/8/2026, 5:08:30 PM
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        count = 0
        seen = set()
        
        for i, num in enumerate(nums):
            if num == key:
                for i in range(max(i-k,0), min(len(nums),i+k+1)):
                    seen.add(i)
        return list(seen)
                
