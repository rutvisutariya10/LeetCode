class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        curr = {}
        l, r = 0, 0
        while r < len(s):
            curr[s[r]] = curr.get(s[r],0) + 1
            while max(curr.values()) + k < sum(curr.values()):
                curr[s[l]] -= 1
                l += 1
        longest = 0
            longest = max(longest,r-l+1)
            r += 1
        return longest
        
