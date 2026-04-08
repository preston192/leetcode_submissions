# Last updated: 4/8/2026, 5:47:26 PM
1class Solution:
2    def totalMoney(self, n: int) -> int:
3        total = 0
4        full_weeks = n // 7
5        stub_week = n - (full_weeks*7)
6
7        for i in range(full_weeks):
8            total += 28
9            total += i*7
10
11        for j in range(stub_week):
12            total += j + 1 + full_weeks
13            
14        return total
15