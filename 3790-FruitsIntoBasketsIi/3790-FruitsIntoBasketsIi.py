# Last updated: 4/8/2026, 5:08:09 PM
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        basket_filled = [False] * len(baskets)
        unplaced = 0

        for fruit in fruits:
            placed = False
            for index, basket in enumerate(baskets):
                if not basket_filled[index] and basket >= fruit:
                    basket_filled[index] = True
                    placed = True
                    break
            if not placed:
                unplaced += 1
        
        return unplaced