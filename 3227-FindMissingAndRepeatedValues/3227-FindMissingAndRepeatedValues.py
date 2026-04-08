# Last updated: 4/8/2026, 5:08:19 PM
class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        flat_grid = [elem for pair in grid for elem in pair]
        count_grid = collections.Counter(flat_grid)
        max_grid = int(max(count_grid, key=count_grid.get))
        missing = set(flat_grid) ^ set([x for x in range(1,len(grid)**2 + 1)])
        return [max_grid, missing.pop()]

