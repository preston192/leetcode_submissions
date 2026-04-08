# Last updated: 4/8/2026, 5:13:30 PM
class Solution(object):
    def mySqrt(self, x):
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid == x:
                return mid
            if mid * mid > x:
                right = mid - 1
            else:
                left = mid + 1
        return right
        