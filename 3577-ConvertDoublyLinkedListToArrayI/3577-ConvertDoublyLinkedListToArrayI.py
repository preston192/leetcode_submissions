# Last updated: 4/8/2026, 5:08:16 PM
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
"""
class Solution:
    def toArray(self, root: 'Optional[Node]') -> List[int]:
        result = []
        curr = root
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result