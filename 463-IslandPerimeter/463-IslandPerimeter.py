# Last updated: 4/8/2026, 5:12:15 PM
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        perimeter = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    if r == 0:
                        up = 0
                    else:
                        up = grid[r - 1][c]
                    if c == 0:
                        left = 0
                    else:
                        left = grid[r][c - 1]
                    if r == row - 1:
                        down = 0
                    else:
                        down = grid[r + 1][c]
                    if c == col - 1:
                        right = 0
                    else:
                        right = grid[r][c + 1]
                    perimeter += 4 - (up + left + down + right)
        return perimeter
