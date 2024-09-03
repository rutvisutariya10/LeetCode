class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        beforeThat = 1
        i = 2
        while i <= n:
            new = prev + beforeThat
            beforeThat = prev
            prev = new
            i += 1
        return prev
            
            
        