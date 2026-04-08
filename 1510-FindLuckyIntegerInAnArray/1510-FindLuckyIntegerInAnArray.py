# Last updated: 4/8/2026, 5:11:17 PM
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = collections.Counter(arr)
        largest = -1
        for key, value in count.items():
            if key == value:
                largest = max(largest, key)
        
        return largest