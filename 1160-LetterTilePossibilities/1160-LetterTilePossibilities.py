# Last updated: 4/8/2026, 5:11:55 PM
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles_l = list(tiles)
        count = 0
        for x in range(1, len(tiles) + 1):
            count += len(set(itertools.permutations(tiles_l, x)))
        return count