# Last updated: 4/8/2026, 5:39:54 PM
class Solution:
    def totalMoney(self, n: int) -> int:
        total = 0
        full_weeks = n // 7
        stub_week = n - (full_weeks*7)

        for i in range(full_weeks):
            total += 28
            total += i*7

        for j in range(stub_week):
            total += j + 1 + full_weeks
            
        return total
