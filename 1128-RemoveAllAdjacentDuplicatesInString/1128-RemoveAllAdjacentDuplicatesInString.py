# Last updated: 4/8/2026, 5:11:55 PM
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for c in s:
            if stack and c == stack[-1]:
                stack.pop()
            else:
                stack.append(c)
        
        return "".join(stack)