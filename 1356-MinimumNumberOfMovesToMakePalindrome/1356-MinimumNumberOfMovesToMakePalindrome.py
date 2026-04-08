# Last updated: 4/8/2026, 5:11:21 PM
class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        moves = 0
        l, r = 0, len(s) - 1
        s_l = list(s)

        while l < r:
            i = r
            while i > l and s_l[i] != s_l[l]:
                i += -1

            if i == l:
                s_l[i], s_l[i + 1] = s_l[i + 1], s_l[i]
                moves += 1

            else:
                while i < r:
                    s_l[i], s_l[i + 1] = s_l[i + 1], s_l[i]
                    i += 1
                    moves += 1

                l += 1
                r += -1

        return moves
            