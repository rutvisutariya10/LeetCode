# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        currBad = -1
        while left <= right:
            middle = (left + right) // 2
            if isBadVersion(middle):
                currBad = middle
                right = middle -1
            else:
                left = middle + 1
        return currBad
                
        