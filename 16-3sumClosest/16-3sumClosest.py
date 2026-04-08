# Last updated: 4/8/2026, 5:14:17 PM
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        distance = float('inf')
        closest_sum = float('inf')
        nums.sort()
        l, r = 0, len(nums) - 1

        for i in range(len(nums)):
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == target:
                    return target
                if abs(nums[i] + nums[l] + nums[r] - target) < distance:
                        distance = abs(nums[i] + nums[l] + nums[r] - target)
                        closest_sum = nums[i] + nums[l] + nums[r]
                elif nums[i] + nums[l] + nums[r] < target:
                    l += 1
                else:
                    r += -1
        return closest_sum
