class Solution:
    def coloredCells(self, n: int) -> int:
        '''
        *
        ***
        *****

        '''
        N = 2 * n - 1
        answer = 0
        for i in range(1,N+1,2):
            answer += i
        for i in range(N-2,0,-2):
            answer += i
        return answer


        