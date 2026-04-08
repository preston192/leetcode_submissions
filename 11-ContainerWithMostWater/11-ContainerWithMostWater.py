# Last updated: 4/8/2026, 5:14:17 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        l, r = 0, len(height)-1

        while l < r:
            volume = min(height[l], height[r]) * (r - l)
            best = max(best, volume)

            if height[l] == height[r]:
                l += 1
                r -= 1
            elif height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
        
        return best
