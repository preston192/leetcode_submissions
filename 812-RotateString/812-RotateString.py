# Last updated: 4/8/2026, 5:12:04 PM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
            
        for i in range(len(goal)):
            if s[i] == goal[0]:
                if s[i:]+s[0:i] == goal:
                    return True
        
        return False
                

