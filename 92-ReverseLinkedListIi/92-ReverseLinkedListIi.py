# Last updated: 4/8/2026, 5:13:25 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or left == right:
            return head
        
        dummy = ListNode(0, head)
        prev = dummy
        curr = None
        next = None
        temp1 = None
        temp2 = None

        for _ in range(left-1):
            prev = prev.next
        
        temp1 = prev
        curr = prev.next
        temp2 = curr

        for _ in range(right-left+1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        temp1.next = prev
        temp2.next = curr

        return dummy.next