        def dfs(r,c):
            if r < 0 or c < 0 or r >= M or c >= N or grid[r][c] == "0" or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        answer = 0
        for row in range(M):
            for col in range(N):
                if (row,col) not in visited and grid[row][col] == "1":
                    dfs(row,col)
                    answer += 1
        
        return answer

