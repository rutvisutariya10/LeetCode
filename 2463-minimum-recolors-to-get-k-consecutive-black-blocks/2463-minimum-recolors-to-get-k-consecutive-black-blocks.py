class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        '''
        ops= 4
        l - r = 7
        [W,B,B,W,W,B,B,W,B,W]
        [0,1,2,3,4,5,6,7,8,9]
               |           |
               l
        '''
        l,r = 0,0
        N = len(blocks)
        ops = 0
        answer = k
        while r < N:
            if blocks[r] == 'W':
                ops += 1
            while r - l >= k:
                if blocks[l] == 'W':
                    ops -= 1
                l += 1  
            if r - l + 1 == k:
                answer = min(answer,ops)     
            r += 1
        return answer
             


        