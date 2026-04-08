# Last updated: 4/8/2026, 5:13:24 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def check(p: TreeNode, q: TreeNode) -> bool:
            if p is None and q is None:
                return True
            if p == None or q == None:
                return False
            return p.val == q.val
        
        deq = deque([(p, q)])
        while deq:
            p, q = deq.popleft()
            if not check(p, q):
                return False
            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))
        return True