# Last updated: 4/8/2026, 5:08:23 PM
class Solution(object):
    def minOperations(self, nums, k):
        collection = set()
        operations = 0

        for num in reversed(nums):
            operations += 1
            if 1 <= num <= k:
                collection.add(num)
            if len(collection) == k:
                return operations

        return operations