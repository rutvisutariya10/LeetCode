class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        curr = set()
        l, r = 0, 0
        while r < len(s):
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            curr.add(s[r])
            longest = max(longest,r-l + 1)
        return longest
            
            r += 1
        
