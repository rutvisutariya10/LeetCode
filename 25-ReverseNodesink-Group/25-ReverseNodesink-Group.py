            # if not available:
            if count < k + 1:
                if curr:
                    tail.next = curr
                break
            
            # keeping track of the tail
            temp = curr
            prev = None
                count += 1
                dist = dist.next
            while curr != dist:
                print(curr.val)
                nn = curr.next
                curr.next = prev
            while dist and count <= k:
                prev = curr
                curr = nn 
            if not start:
                start = prev
            tail = temp
            if tail:
                tail.next = prev
