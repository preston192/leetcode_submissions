# Last updated: 4/8/2026, 6:03:02 PM
1import heapq
2from collections import defaultdict
3
4class Solution:
5    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
6        arr.sort()
7        distance = defaultdict(list)
8        for i in range(len(arr)-1):
9            distance[arr[i+1]-arr[i]].append([arr[i],arr[i+1]])
10
11        groups = [(d, nums) for d, nums in distance.items()]
12        heapq.heapify(groups)
13        d, result = heapq.heappop(groups)
14
15        return result
16
17