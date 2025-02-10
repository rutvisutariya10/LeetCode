        for i in s:
        for i in t:
        for i in s_dict.keys():
            if i not in t_dict or s_dict[i] != t_dict[i]:
                return False
            s_dict[i] = s_dict.get(i, 0) + 1
            t_dict[i] = t_dict.get(i, 0) + 1
        t_dict = {}
        s_dict = {}
            return False
        if S != T:
        S,T = len(s),len(t)
    def isAnagram(self, s: str, t: str) -> bool:
class Solution:
