# Last updated: 4/8/2026, 5:11:21 PM
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_l = list(s)
        stack = []
        
        for i, c in enumerate(s_l):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    s_l[i] = None
        
        while stack:
            s_l[stack.pop()] = None

        return "".join(c for c in s_l if c != None)