# Last updated: 4/8/2026, 5:11:15 PM
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        largest = max(candies)
        for i, candy in enumerate(candies):
            if candy + extraCandies >= largest:
                result[i] = True
        return result
