            for idx,x in enumerate(st):
                nn = number - int(st[:idx+1])
                if nn >= 0 and partition(st[idx+1:],nn):
                    return True
            return False
   
        answer = 0
        for num in range(1,n+1):
            sq = num * num
            digits = ""
            while sq > 0:
                digits += str(sq%10)
                sq //= 10
            if partition(digits[::-1],num):
                answer += (num*num)
        return answer
        
                return True
