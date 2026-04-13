# Last updated: 4/12/2026, 9:57:21 PM
class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "*":
                stack.append(c)
            else:
                stack.pop()
        
        return "".join(stack)