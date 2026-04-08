# Last updated: 4/8/2026, 5:12:26 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # bucket sort

        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in freq.items():
            buckets[count].append(num)

        ans = []

        for count in range(len(nums), 0, -1):
            if buckets[count]:
                for num in buckets[count]:
                    ans.append(num)
                    if len(ans) == k:
                        return ans