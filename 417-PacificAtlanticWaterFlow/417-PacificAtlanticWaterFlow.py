        for j in range(N):
            dfs(i,N-1,heights[i][N-1],atlantic)
            dfs(0,j,heights[0][j],pacific)
            dfs(M-1,j,heights[M-1][j],atlantic)
        for i in range(M):
            for j in range(N):
                if (i,j) in pacific and (i,j) in atlantic:
        res = []
                    res.append([i,j])

        return res
        
