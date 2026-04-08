# Last updated: 4/8/2026, 5:15:00 PM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        broken = set(brokenLetters)
        count = 0
        for word in words:
            if not set(word) & broken:
                count += 1

        return count



            