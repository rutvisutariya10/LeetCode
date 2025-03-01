
        Each time you can add either 1 or 2
        S(i) = ith stair,  1 <= i <= n
        S(i) = S(i-1)
        Base = 
        '''
        prev = 1
        before_that = 2
        answer = 0
        for i in range(3,n+1):
            answer = prev + before_that
            before_that, prev = prev, answer
        if n == 1:
            return 1
        if n == 2:
            return 2
        return answer

