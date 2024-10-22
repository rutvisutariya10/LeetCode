class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        M,N = len(grid),len(grid[0])
        count = 0
        visited = set()
        def findIsland(r,c):
            if r < 0 or r >= M or c < 0 or c >= N or (r,c) in visited or grid[r][c] == "0":
                return 
            visited.add((r,c))
            findIsland(r-1,c)
            findIsland(r+1,c)
            findIsland(r,c-1)
            findIsland(r,c+1)
        
        for i in range(M):
            for j in range(N):
                if (i,j) not in visited and grid[i][j] == "1":
                    count += 1
                    findIsland(i,j)
        
        return count
        
        