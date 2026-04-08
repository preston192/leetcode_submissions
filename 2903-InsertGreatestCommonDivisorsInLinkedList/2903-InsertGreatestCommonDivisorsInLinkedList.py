# Last updated: 4/8/2026, 5:08:26 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
            return a
            
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head

        prev = head
        curr = prev.next
        next = curr.next

        while curr:
            gcd = ListNode(math.gcd(prev.val, curr.val))
            prev.next = gcd
            gcd.next = curr

            prev = curr
            curr = curr.next
        
        return head
