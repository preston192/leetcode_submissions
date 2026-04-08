# Last updated: 4/8/2026, 5:11:17 PM
class Solution:
    def countLargestGroup(self, n: int) -> int:
        groups = collections.Counter()

        for i in range(1, n + 1):
            x, curr = i, 0
            while x:
                curr += x % 10
                x //= 10
            groups[curr] += 1

        max_size = max(groups.values())
        return sum(1 for size in groups.values() if size == max_size)