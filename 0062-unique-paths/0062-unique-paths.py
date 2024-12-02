class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        answer = [[0]*n]*m
        for i in range(m):
            answer[i][0] = 1
        for i in range(n):
            answer[0][i] = 1
        
        for i in range(1,m):
            for j in range(1,n):
                answer[i][j] = answer[i-1][j] + answer[i][j-1]
        
        return answer[m-1][n-1]
        
        
                
        