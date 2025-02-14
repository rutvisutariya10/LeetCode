        while l1:
            value = l1.val + carry
            if value // 10 != 0:
                carry = 1
            else:
                carry = 0
            nn = ListNode(value%10,None)
            prev.next = nn
            prev = prev.next
            l1 = l1.next
        while l2:
            value = l2.val + carry
            if value // 10 != 0:
                carry = 1
            else:
                carry = 0
            nn = ListNode(value%10,None)
            prev.next = nn
            prev = prev.next
            l2 = l2.next
        return dummy.next
        if carry == 1:
            nn = ListNode(1,None)
            prev.next = nn
