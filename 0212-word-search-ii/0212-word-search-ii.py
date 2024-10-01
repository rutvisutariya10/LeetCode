class Tries:
    def __init__(self):
        self.children = {}
        self.endNode = False
    def addWord(self, word: str) -> None:
        curr = self
        for i in word:
            if i not in curr.children:
                curr.children[i] = Tries()
            curr = curr.children[i]
        curr.endNode = True
                

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        # Creating trie of Words
        trie = Tries()
        for word in words:
            trie.addWord(word)
          
        ROWS,COLS = len(board),len(board[0])
        
        visited = set()
        result = set()
        def bfs(row,col,curr,node):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or (row,col) in visited or board[row][col] not in node.children:
                return
            
            visited.add((row,col))
            node = node.children[board[row][col]]
            curr += board[row][col]
            if node.endNode:
                result.add(curr)
            bfs(row - 1, col,curr,node)
            bfs(row + 1, col,curr,node) 
            bfs(row, col - 1,curr,node)
            bfs(row, col + 1,curr,node)
            curr = curr[:-1]
            visited.remove((row,col))
            
            
        for i in range(ROWS):
            for j in range(COLS):
                bfs(i,j,"",trie)
        
        return list(result)
        
        