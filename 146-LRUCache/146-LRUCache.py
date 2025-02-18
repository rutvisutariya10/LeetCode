    def get(self, key: int) -> int:

        node.next.prev = node.prev        
        node.prev.next = node.next
    def remove(self, node: ListNode) -> None:
        self.newest.prev,node.next = node,self.newest
        self.newest.prev.next, node.prev = node, self.newest.prev
    def insert(self,node: ListNode) -> None:

        self.newest.prev = self.oldest
