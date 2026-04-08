# Last updated: 4/8/2026, 5:12:08 PM
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        boundary = [1]
        result = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                boundary[-1] += 1
            else:
                boundary.append(1) 

        for i in range(1, len(boundary)):
             result += min(boundary[i - 1], boundary[i])
        
        return result