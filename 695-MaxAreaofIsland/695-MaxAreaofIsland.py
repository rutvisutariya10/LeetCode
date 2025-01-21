        def dfs(r,c):
        visited = set()
            if r < 0 or c < 0 or r >= M or c >= N or grid[r][c] == 0 or (r,c) in visited:
                return 0 
            visited.add((r,c))
            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)
        for row in range(M):
            for col in range(N):
        M, N = len(grid), len(grid[0])
                if (row,col) not in visited and grid[row][col] == 1:
                    answer = max(answer,dfs(row,col))
        answer = 0
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
class Solution:
        return answer
        
