# Last updated: 4/8/2026, 5:08:31 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head.next
        total = 0
        dummy = head
        temp = dummy
        # traverse the list, if detect zero store as temp and start loop summing up until detecting another zero
        # store sum in temp (currently zero), point it to the next zero and repeat

        while curr:
            if curr.val == 0:
                temp.next = ListNode(total)
                total = 0
                temp = temp.next
            if curr.val != 0:
                total += curr.val
            curr = curr.next
        
        return dummy.next