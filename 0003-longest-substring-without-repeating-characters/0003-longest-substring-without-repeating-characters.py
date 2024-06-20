class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        strLen = len(s)
        if strLen == 0:
            return 0
        if strLen == 1:
            return 1
        inString = set()
        left = 0
        right = 0
        maxLen = 1
        while right < strLen:
            if s[right] in inString:
                while s[left] != s[right]:
                    inString.remove(s[left])
                    left += 1
                left += 1
            else:
                inString.add(s[right])
                maxLen = max(len(inString),maxLen)
            right += 1
        return maxLen



        