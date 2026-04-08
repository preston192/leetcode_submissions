# Last updated: 4/8/2026, 5:08:16 PM
class Solution:
    def kthCharacter(self, k: int) -> str:
        shifts = (k - 1).bit_count()
        return chr(ord('a') + (shifts % 26))