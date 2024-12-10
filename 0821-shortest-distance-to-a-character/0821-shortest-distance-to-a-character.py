class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        answer = [-1] * len(s)
        idx = []
        r = 0
        while r < len(s):
            if s[r] == c:
                idx.append(r)
            r += 1
        
        l, r = 0, 0
        for i in range(len(s)):
            if i > idx[r] and r < len(idx) - 1:
                l = r
                r += 1
            answer[i] = min(abs(idx[l] - i),abs(idx[r] - i))
        
        return answer
                
        
        
        
        
        