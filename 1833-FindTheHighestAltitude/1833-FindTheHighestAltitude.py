# Last updated: 4/8/2026, 5:08:40 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        current = 0
        for num in gain:
            current += num
            highest = max(highest, current)
        return highest