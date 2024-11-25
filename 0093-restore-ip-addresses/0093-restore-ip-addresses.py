class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Handle leadin 0
        # Handle greater than 255
        # Must contain 3 decimals?
        # MAKE A LIST OF NUMBERS AND THEN APPENd OR HAVE A TEMP WHERE APPEND?
        # can only use upto 3 digits, handle all three toether?
        
        N = len(s)
        answer = []
        def dfs(i,curr,nos):
            if i == N and nos == 4:
                answer.append(curr[:-1])
                return
            if i == N or nos > 4:
                return
            dfs(i+1,curr+s[i]+".",nos+1)
            if s[i] != "0":
                if i < N - 1:
                    dfs(i+2,curr+s[i:i+2]+".",nos+1)
                if i < N - 2 and int(s[i:i+3]) <= 255:
                    dfs(i+3,curr+s[i:i+3]+".",nos+1)
        dfs(0,"",0)
        return answer
            
                
            
            
            
            
        