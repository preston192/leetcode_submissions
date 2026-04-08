# Last updated: 4/8/2026, 5:12:13 PM
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        curr = w
        cap_heap = [(v, i) for i, v in enumerate(capital)]
        heapify(cap_heap)
        pro_heap = []
        
        for _ in range(k):
            while cap_heap and cap_heap[0][0] <= curr:
                _, i = heappop(cap_heap)
                heappush(pro_heap, -profits[i])

            if not pro_heap:
                return curr

            else: 
                curr += -heappop(pro_heap)

        return curr