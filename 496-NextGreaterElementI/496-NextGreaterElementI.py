# Last updated: 4/8/2026, 5:12:14 PM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        mapping = {val: i for i, val in enumerate(nums2)}

        for i in range(len(nums1)):
            for j in range(mapping[nums1[i]]+1, len(nums2)):
                if nums2[j] > nums1[i]:
                    result.append(nums2[j])
                    break
            if len(result) < i+1:
                result.append(-1)
            

        return result