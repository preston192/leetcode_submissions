# Last updated: 4/8/2026, 5:13:38 PM
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    empties.append((r, c))
                else:
                    val = board[r][c]
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(idx: int) -> bool:
            if idx == len(empties):
                return True

            r, c = empties[idx]
            b = (r // 3) * 3 + (c // 3)

            for ch in "123456789":
                if ch in rows[r] or ch in cols[c] or ch in boxes[b]:
                    continue

                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[b].add(ch)

                if backtrack(idx + 1):
                    return True

                board[r][c] = "."
                rows[r].remove(ch)
                cols[c].remove(ch)
                boxes[b].remove(ch)

            return False

        backtrack(0)