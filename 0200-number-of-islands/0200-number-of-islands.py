class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        number = 0
        ROWS, COLS = len(grid), len(grid[0])
        path = set()
        
        def dfs(r,c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0" or (r,c) in path:
                return
            path.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in path:
                    number += 1
                    dfs(r,c)
        return number
        