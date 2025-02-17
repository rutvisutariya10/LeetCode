            head = ListNode()
            prev = head
            while list1 and list2:
                if list1.val <= list2.val:
                    prev.next = list1
                    list1 = list1.next
                else:
                    prev.next = list2
                    list2 = list2.next
            if list1:
                prev.next = list1
            if list2:
                prev.next = list2
            return head.next
        list1 = lists[0]
                prev = prev.next
