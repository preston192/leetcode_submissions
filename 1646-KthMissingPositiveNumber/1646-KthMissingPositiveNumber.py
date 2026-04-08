# Last updated: 4/8/2026, 5:08:42 PM
class Solution(object):
    def findKthPositive(self, arr, k):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if (arr[mid] - mid - 1) < k:
                left = mid + 1
            else:
                right = mid - 1
        return left + k            