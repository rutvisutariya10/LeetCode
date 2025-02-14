            if head.next:
                mapp[head].next = mapp[head.next]
            if head.random:
                mapp[head].random = mapp[head.random]
            head = head.next

        return mapp[ans] if ans else None
        
        
        while head:
        ans = head
            curr = curr.next
            mapp[curr] = nn
            nn = Node(curr.val)
        
