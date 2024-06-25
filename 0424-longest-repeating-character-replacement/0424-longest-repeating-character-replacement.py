class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        s_len = len(s)
        seen = {}
        left = 0
        right = 0
        total = 0
        currMax = 0
        while right < s_len:
            seen[s[right]] = seen.get(s[right],0) + 1
            total += 1
            while (total - max(seen.values())) > k:
                seen[s[left]] -= 1
                left += 1
                total -= 1
            currMax = max(currMax,total)
            right += 1
        return currMax
            
        