# Last updated: 4/8/2026, 5:41:14 PM
1class Solution:
2    def totalMoney(self, n: int) -> int:
3        total = 0
4        full_weeks = n // 7
5        stub_week = n - (full_weeks*7)
6
7        for i in range(full_weeks):
8            total += 28 + i*7
9
10        for j in range(stub_week):
11            total += j + 1 + full_weeks
12            
13        return total
14