# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr, prev, start = head, None, None
        while curr:
            temp = curr.next
            count = 1
            while temp and temp.val == curr.val:
                count += 1
                temp = temp.next
            if count == 1:
                if prev:
                    prev.next = curr
                    prev = prev.next
                else:
                    prev, start = curr, curr
            curr = temp
        if prev:
            prev.next = None
        return start
                    
                        
                
                
            
                
        