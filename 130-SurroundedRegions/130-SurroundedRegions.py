        for i in range(M):
            dfs(r,c-1)
            dfs(r,c+1)
            dfs(r+1,c)
            dfs(r-1,c)
            unsurrounded.add((r,c))
                return
            if r < 0 or c < 0 or r >= M or c >= N or (r,c) in unsurrounded or board[r][c] == "X":
        def dfs(r,c):
        unsurrounded = set()
        M, N = len(board), len(board[0])
        """
        Do not return anything, modify board in-place instead.
        """
            print(r,c)
            dfs(i,0)
            dfs(i,N-1)
