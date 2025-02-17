        M, N = len(s1), len(s2)
    def checkInclusion(self, s1: str, s2: str) -> bool:
class Solution:
        pattern = {}
        for c in s1:
            pattern[c] = pattern.get(c,0) + 1
        l, r = 0, 0
        find = collections.defaultdict(int)
        while r < len(s2):
            print(find,s2[r])
            if s2[r] not in pattern:
                find = collections.defaultdict(int)
                r += 1
                l = r
                continue
            find[s2[r]] += 1
            while find[s2[r]] > pattern[s2[r]]:
                find[s2[l]] -= 1
                l += 1
            if r - l + 1 == M:
                return True
