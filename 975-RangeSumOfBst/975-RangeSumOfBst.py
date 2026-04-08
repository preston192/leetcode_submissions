# Last updated: 4/8/2026, 5:12:01 PM
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rangeSumBST(self, root, low, high):
        def dfs(root):
            if not root:
                return 0
            if root.val < low:
                return dfs(root.right)
            if root.val > high:
                return dfs(root.left)
            if root.val >= low and root.val <= high:
                return root.val + dfs(root.left) + dfs(root.right)
        
        return dfs(root)