class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number = 0
        ROWS, COLS = len(grid), len(grid[0])
        path = set()
        
        # def dfs(r,c):
        #     if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0" or (r,c) in path:
        #         return
        #     path.add((r,c))
        #     dfs(r-1,c)
        #     dfs(r+1,c)
        #     dfs(r,c-1)
        #     dfs(r,c+1)
        
        def bfs(r,c):
            
            queue = collections.deque()
            path.add((r,c))
            queue.append((r,c))
            while queue:
                R,C = queue.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr,dc in directions:
                    x = R + dr
                    y = C + dc
                    if x >= 0 and x < ROWS and y >= 0 and y < COLS and (x,y) not in path and grid[x][y] == "1":
                        path.add((x,y))
                        queue.append((x,y))
            
            
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in path:
                    number += 1
                    bfs(r,c)
        return number
        