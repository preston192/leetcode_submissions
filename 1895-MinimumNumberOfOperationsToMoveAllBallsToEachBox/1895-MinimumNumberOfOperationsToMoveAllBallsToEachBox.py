# Last updated: 4/8/2026, 5:08:38 PM
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        result = [0] * n
        
        left_moves = 0
        left_balls = 0
        right_moves = 0
        right_balls = 0

        for i in range(n):
            result[i] += left_moves
            left_balls += int(boxes[i])
            left_moves += left_balls
        
        for j in range(n-1, -1, -1):
            result[j] += right_moves
            right_balls += int(boxes[j])
            right_moves += right_balls
        
        return result
