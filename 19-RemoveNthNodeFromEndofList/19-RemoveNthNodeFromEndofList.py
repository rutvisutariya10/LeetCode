# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left = ListNode(0,head)
        count = 1
        while count <= n:
            head = head.next
            count += 1
        while head:
            right = right.next
            head = head.next
        return left.next
        
        right.next = right.next.next
        right = left
        
