class Solution:
    def clearDigits(self, s: str) -> str:
        ''' 
        a3bb3ccc3
        bcc        
        '''

        ans = ""
            

            
                
        for i in s:
            if i.isnumeric():
                ans = ans[:-1]
            else:
                ans += i
        return ans

