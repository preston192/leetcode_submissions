# Last updated: 4/8/2026, 5:11:20 PM
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_s = set(nums1)
        nums2_s = set(nums2)
        return [list(nums1_s - nums2_s), list(nums2_s - nums1_s)]