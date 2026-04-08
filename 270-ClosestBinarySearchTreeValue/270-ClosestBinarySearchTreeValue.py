# Last updated: 4/8/2026, 5:12:32 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        best = root.val
        def dfs(node):
            nonlocal best
            if not node:
                return
            if (abs(node.val - target) < abs(best - target)) or \
                (abs(node.val - target) == abs(best - target) and node.val < best):
                best = node.val
            if node.val > target:
                dfs(node.left)
            if node.val < target:
                dfs(node.right)
        dfs(root)
        return best