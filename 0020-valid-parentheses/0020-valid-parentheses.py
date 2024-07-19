class Solution:
    def isValid(self, s: str) -> bool:
        l = []
        for i in s:
            if i in "({[":
                l += i
                continue
            if len(l) == 0:
                return False
            if i == ")":
                if l.pop() != "(":
                    return False
            elif i == "}":
                if l.pop() != "{":
                    return False
            else:
                if l.pop() != "[":
                    return False
        if len(l) != 0:
            return False
        return True
            

                
            

        