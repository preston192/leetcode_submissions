# Last updated: 4/8/2026, 5:13:34 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for interval in intervals:
            if result[-1][1] >= interval[0]:
                result[-1] = [result[-1][0], max(result[-1][1], interval[1])]
            else:
                result.append(interval)
        return result