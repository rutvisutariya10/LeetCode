class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(name) == 1 and len(typed) == 1:
            return name[0] == typed[0]
        l, r = 0, 0
        while r < len(typed) and l < len(name):
            if name[l] == typed[r]:
                while r < len(typed) and l < len(name) and name[l] == typed[r]:
                    l += 1
                    r += 1
                while r < len(typed) and r > 0 and typed[r-1] == typed[r]:
                    r += 1
                if l == len(name) and r == len(typed):
                    return True  
            else:
                return False
        return False
                
        