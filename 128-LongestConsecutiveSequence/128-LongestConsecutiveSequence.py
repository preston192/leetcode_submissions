# Last updated: 4/8/2026, 5:13:20 PM
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count = 0
        nums_set = set(nums)
        for n in nums_set:
            if n - 1 not in nums_set:
                curr_num = n
                curr_count = 1

                while curr_num + 1 in nums_set:
                    curr_num += 1
                    curr_count += 1
            
                max_count = max(max_count, curr_count)
        
        return max_count