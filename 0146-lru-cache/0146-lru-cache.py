class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left, self.right = Node(-1,-1), Node(-1,-1)
        self.cache = {}
        self.left.next, self.right.prev = self.right, self.left
        
    def removeNode(self,Node):
        prev, next = Node.prev, Node.next
        Node.prev.next = next
        Node.next.prev = prev
        
    def insertNode(self,Node):
        self.right.prev.next = Node
        Node.prev = self.right.prev
        self.right.prev = Node
        Node.next = self.right

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        # Update LRU
        self.removeNode(self.cache[key])
        self.insertNode(self.cache[key])
        return self.cache[key].val
            
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insertNode(self.cache[key])
        
        # Capacity
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.removeNode(lru) 
            
            del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)