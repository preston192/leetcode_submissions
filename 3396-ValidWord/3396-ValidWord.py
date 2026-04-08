# Last updated: 4/8/2026, 5:08:17 PM
class Solution:
    def isValid(self, word: str) -> bool:
        vowel_check = 0
        consonant_check = 0 

        if not word.isalnum() or len(word) < 3:
            return False

        for c in word:
            if c.lower() in "aeiou":
                vowel_check += 1
                continue
            elif c.isalpha():
                consonant_check += 1
        
        if vowel_check > 0 and consonant_check > 0:
            return True

        return False