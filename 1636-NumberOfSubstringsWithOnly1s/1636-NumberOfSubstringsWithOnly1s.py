# Last updated: 4/8/2026, 5:08:44 PM
class Solution:
    def numSub(self, s: str) -> int:
        current = 0
        total = 0

        for c in s:
            if c == "1":
                current += 1
                continue
            else:
                total += (current * (current+1))/2
                current = 0
        if current > 0:
            total += (current * (current+1))/2
        total %= 10**9 + 7
        return int(total)