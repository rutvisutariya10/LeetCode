        l, r = 0, len(self.time[key]) - 1
        ''' 
        2
        [1,3]
        '''
        while l < r:
            middle = (l + r + 1) // 2
            if timestamp >= self.time[key][middle][0]:
                l = middle
            return ""
        if not self.time[key] or self.time[key][0][0] > timestamp:
    def get(self, key: str, timestamp: int) -> str:

