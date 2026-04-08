# Last updated: 4/8/2026, 5:08:37 PM
from collections import deque

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        buildings = deque([len(heights) - 1])
        highest = heights[-1]
        for i in range(len(heights) - 1, -1, -1):
            if heights[i] > highest:
                buildings.appendleft(i)
                highest = heights[i]
        return list(buildings)
