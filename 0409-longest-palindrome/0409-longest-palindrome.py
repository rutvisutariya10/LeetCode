class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for i in s:
            count[i] = count.get(i,0) + 1
        singleUsed = False
        answer = 0
        for i in count.keys():
            if count[i] % 2 == 0:
                answer += count[i]
            else:
                answer += count[i] - 1
                if not singleUsed:
                    answer += 1
                    singleUsed = True
        return answer
                
        
        