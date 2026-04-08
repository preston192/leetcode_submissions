# Last updated: 4/8/2026, 5:08:37 PM
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        used = set(sentence)
        return len(used) == 26