class Solution:
    def isHappy(self, n: int) -> bool:
        count = collections.defaultdict(int)
        while n > 0:
            new_n = 0
            while n > 0:
                temp = n % 10
                new_n += temp*temp
                n //= 10
            if new_n == 1:
                return True
            if new_n // 10 == 0:
                count[new_n] += 1
                if count[new_n] > 1:
                    return False
            n = new_n
            
        