# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        heap = []
        for i,nodeK in enumerate(lists):
            if nodeK:
                heapq.heappush(heap,(nodeK.val,i,nodeK))
        while heap:
            newNode = heapq.heappop(heap)
            curr.next = newNode[2]
            if newNode[2].next:
                heapq.heappush(heap,(newNode[2].next.val,newNode[1],newNode[2].next))
            curr = curr.next
        return dummy.next
                            
            
            