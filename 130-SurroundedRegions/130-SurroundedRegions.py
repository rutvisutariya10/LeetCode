            pathVisited.add((r,c))
            return dfs(r-1,c) and dfs(r+1,c) and dfs(r,c-1) and dfs(r,c+1)
        
        for row in range(M):
            for col in range(N):
                if board[row][col] == "O" and (row,col) not in visited:
                    pathVisited = set()
            visited.add((r,c))
                return False
            if board[r][c] == "O" and (r == 0 or c == 0 or r == M - 1 or c == N - 1):
                return True
            if r < 0 or c < 0 or r >= M or c >= N or (r,c) in pathVisited or board[r][c] == "X":
        def dfs(r,c):
        visited, pathVisited = set(),set()
        M, N = len(board), len(board[0])
        """
        Do not return anything, modify board in-place instead.
