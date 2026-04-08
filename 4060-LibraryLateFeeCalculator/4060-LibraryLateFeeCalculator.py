# Last updated: 4/8/2026, 5:08:10 PM
class Solution:
    def lateFee(self, daysLate: List[int]) -> int:
        return sum(1 if x == 1 else (3*x if x > 5 else 2*x) for x in daysLate)