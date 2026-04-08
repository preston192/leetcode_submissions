# Last updated: 4/8/2026, 5:08:24 PM
class Solution(object):
    def isAcronym(self, words, s):
        return len(words) == len(s) and s == ''.join(word[0] for word in words)
