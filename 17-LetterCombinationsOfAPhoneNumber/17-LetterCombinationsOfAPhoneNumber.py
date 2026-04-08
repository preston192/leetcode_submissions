# Last updated: 4/8/2026, 5:15:04 PM
from itertools import product
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {"2": ["a", "b", "c"], 
        "3": ["d", "e", "f"], 
        "4": ["g", "h", "i"], 
        "5": ["j", "k", "l"], 
        "6": ["m", "n", "o"], 
        "7": ["p", "q", "r", "s"], 
        "8": ["t", "u", "v"], 
        "9": ["w", "x", "y", "z"]}

        if not digits:
            return []

        pools = [phone[d] for d in digits]
        combos = ["".join(t) for t in product(*pools)]
        return combos