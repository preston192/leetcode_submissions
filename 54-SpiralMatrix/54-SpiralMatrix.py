# Last updated: 4/8/2026, 5:13:35 PM
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, cols - 1
        top, bot = 0, rows - 1
        res = []

        while len(res) < rows * cols:
            # right
            if top <= bot:
                for x in range(left, right + 1):
                    res.append(matrix[top][x])
                top += 1

            # down
            if left <= right:
                for y in range(top, bot + 1):
                    res.append(matrix[y][right])
                right -= 1

            # left
            if top <= bot:
                for x in range(right, left - 1, -1):
                    res.append(matrix[bot][x])
                bot -= 1

            # up
            if left <= right:
                for y in range(bot, top - 1, -1):
                    res.append(matrix[y][left])
                left += 1

        return res
