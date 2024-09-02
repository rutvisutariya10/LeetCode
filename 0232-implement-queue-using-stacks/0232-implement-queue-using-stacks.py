class MyQueue:
    def __init__(self):
        self.inQueue = []
        self.tempQueue = []

    def push(self, x: int) -> None:
        while self.inQueue:
            self.tempQueue.append(self.inQueue.pop())
        self.inQueue.append(x)
        while self.tempQueue:
            self.inQueue.append(self.tempQueue.pop())

    def pop(self) -> int:
        return self.inQueue.pop()
        

    def peek(self) -> int:
        return self.inQueue[-1]

    def empty(self) -> bool:
        if self.inQueue:
            return False
        return True


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()