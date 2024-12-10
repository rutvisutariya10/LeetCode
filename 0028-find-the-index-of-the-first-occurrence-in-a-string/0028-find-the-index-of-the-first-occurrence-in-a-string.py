class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lps = [0] * len(needle)
        prevLps, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prevLps]:
                lps[i] = prevLps + 1
                i += 1
                prevLps += 1
            elif prevLps == 0:
                lps[i] = 0
                i += 1
            else:
                prevLps = lps[prevLps - 1]
        l, r = 0, 0
        while r < len(haystack):
            if needle[l] == haystack[r]:
                l += 1
                r += 1
            else:
                if l != 0:
                    l = lps[l - 1]
                else:
                    r += 1
            if l == len(needle):
                return r - len(needle)
        return -1
        
        