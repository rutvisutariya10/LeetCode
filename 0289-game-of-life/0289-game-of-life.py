class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board),len(board[0])
        
        def aliveNeighbors(row,col):
            neigh_rows = [-1,-1,-1,0,0,0,1,1,1]
            neigh_cols = [-1,0,1,-1,0,1,-1,0,1]
            alive = 0
            for i in range(9):
                n_x = row + neigh_rows[i]
                n_y = col + neigh_cols[i]
                if n_x >= 0 and n_x < ROWS and n_y >= 0 and n_y < COLS:
                    if n_x == row and n_y == col:
                        continue
                    if board[n_x][n_y] in [1,3]:
                        alive += 1
            return alive
        
        
        for r in range(ROWS):
            for c in range(COLS):
                alive = aliveNeighbors(r,c)
                if board[r][c] == 0:
                    if alive == 3:
                        board[r][c] = 2
                else:
                    if alive < 2 or alive > 3:
                        board[r][c] = 3
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 2:
                    board[r][c] = 1
                elif board[r][c] == 3:
                    board[r][c] = 0
                    
        return board