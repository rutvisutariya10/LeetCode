class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = "abc"
        answer = []
        def dfs(idx,st):
            if idx == n:
                answer.append(st)
                return 
            for c in letters:
                if idx != 0 and st[-1] == c:
                    continue
                dfs(idx+1,st+c)
            return
        dfs(0,"")
        return answer[k-1] if k <= len(answer) else ""
            
        
