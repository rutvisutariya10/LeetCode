        self.nums.append(num)
        if self.count == 0:
            self.prod.append(num)
        else:
            if num == 0:
                self.prod = [0] * (self.count + 1)
            else:
                if self.prod[-1] == 0:
                    self.prod.append(num)
                else:
                    self.prod.append(self.prod[-1]*num)
        self.count += 1

    def getProduct(self, k: int) -> int:
        idx = self.count - k
        if idx == 0:
            if self.prod[0] == 0:
                return 0
            return self.prod[-1]
        elif self.prod[idx] == 0:
            return 0
        if self.prod[idx-1] == 0:
            return self.prod[-1]
