# Last updated: 4/8/2026, 5:13:21 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        low = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < low:
                low = prices[i]
            elif prices[i] - low > best:
                best = prices[i] - low

        return best