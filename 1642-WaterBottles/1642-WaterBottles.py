# Last updated: 4/8/2026, 5:08:43 PM
class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty = numBottles
        count = numBottles

        while empty >= numExchange:
            new_full = empty // numExchange
            count += new_full
            empty = empty % numExchange + new_full

        return count