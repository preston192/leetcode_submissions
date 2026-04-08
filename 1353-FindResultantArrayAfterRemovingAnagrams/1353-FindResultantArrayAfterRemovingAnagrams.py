# Last updated: 4/8/2026, 5:11:22 PM
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = []
        prev = ""

        for word in words:
            s = "".join(sorted(word))
            if s != prev:
                result.append(word)
                prev = s

        return result