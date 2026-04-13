# Last updated: 4/12/2026, 9:58:10 PM
import heapq
from collections import defaultdict

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        distance = defaultdict(list)
        for i in range(len(arr)-1):
            distance[arr[i+1]-arr[i]].append([arr[i],arr[i+1]])

        groups = [(d, nums) for d, nums in distance.items()]
        heapq.heapify(groups)
        d, result = heapq.heappop(groups)

        return result

