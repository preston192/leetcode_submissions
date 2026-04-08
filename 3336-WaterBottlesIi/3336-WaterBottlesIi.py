# Last updated: 4/8/2026, 5:08:18 PM
class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        exchange = numExchange
        empty = numBottles
        count = numBottles

        while empty >= exchange:
            count += 1
            empty = empty - exchange + 1
            exchange += 1
        
        return count