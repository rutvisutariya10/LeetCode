#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

'''
prev.next = list1
list1 = list1.next

'''
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
