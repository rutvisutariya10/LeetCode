        for k,v in self.queue:

    def put(self, key: int, value: int) -> None:
        for k,v in self.queue:
            if k == key:
                return v
        return -1
                self.queue.remove((k,v))
                self.queue.append((k,v))
            if k == key:
                self.queue.remove((k,v))
        self.queue.append((key,value))
        while len(self.queue) > self.cap:
    def get(self, key: int) -> int:

        
            self.queue.popleft()
        


                break
