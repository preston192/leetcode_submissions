# Last updated: 4/8/2026, 5:08:34 PM
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for sentence in sentences:
            max_words = max(len(sentence.split()), max_words)
        return max_words