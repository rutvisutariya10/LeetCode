class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answer = []
        def dfs(o,c,curr):
            if c > n or o > n:
                return
            if o == n:
                answer.append(curr + ")"*(o-c))
                return 
            dfs(o+1,c,curr+"(")
            if c < o:
                dfs(o,c+1,curr+")")
        
        dfs(1,0,"(")
        return answer
                    
                    
            
        