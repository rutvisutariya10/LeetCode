            if r < 0 or c < 0 or r >= M or c >= N or (r,c) in visited or board[r][c] == "X":
                return True
            if board[r][c] == "O" and (r == 0 or c == 0 or r == M - 1 or c == N - 1):
                return False
            visited.add((r,c))
            pathVisited.add((r,c))
            return dfs(r-1,c) and dfs(r+1,c) and dfs(r,c-1) and dfs(r,c+1)
        
        def dfs(r,c):
        M, N = len(board), len(board[0])
        visited, pathVisited = set(),set()
        Do not return anything, modify board in-place instead.
        """
        """
    def solve(self, board: List[List[str]]) -> None:
        for row in range(M):
            for col in range(N):
