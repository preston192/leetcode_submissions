# Last updated: 4/8/2026, 5:14:21 PM
import heapq
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        result = nums1 + nums2
        result.sort()
        n = len(nums1)
        m = len(nums2)
        min_heap = [-x for x in result[:(n+m) // 2:]]
        max_heap = result[(n+m) // 2::]

        heapify(min_heap)
        heapify(max_heap)

        if (n+m) % 2 == 1:
            return max_heap[0]
        else:
            return (-min_heap[0] + max_heap[0]) / 2.0
