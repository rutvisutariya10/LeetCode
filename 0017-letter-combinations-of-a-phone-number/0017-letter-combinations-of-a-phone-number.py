class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        match = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        N = len(digits)
        if N == 0:
            return []
        answer = []
        def dfs(i,current):
            if i == N:
                answer.append(current)
                return
            
            for s in match[digits[i]]:
                dfs(i+1,current+s)
        
        dfs(0,"")
        return answer
                
            
            