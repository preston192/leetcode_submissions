# Last updated: 4/8/2026, 5:08:25 PM
class Solution(object):
    def countPairs(self, nums, target):
  
        nums.sort()
        
        # Initialize pointers and the count variable
        left = 0
        right = len(nums) - 1
        count = 0
        
        # Use the two-pointer technique to count valid pairs
        while left < right:
            if nums[left] + nums[right] < target:
                # Since the array is sorted, all elements between left and right
                # will form a valid pair with nums[left]
                count += right - left
                left += 1  # Move the left pointer to explore new pairs
            else:
                right -= 1  # Otherwise, move the right pointer to reduce the sum
        
        return count