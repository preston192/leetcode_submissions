# Last updated: 4/8/2026, 5:12:26 PM
class Solution(object):
    def intersection(self, nums1, nums2):
        return list(set(nums1) & set(nums2))
        