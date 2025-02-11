class Solution:
    def isValid(self, s: str) -> bool:
        dict = {'(':')', '{':'}', '[':']'} 
        stack = []
        for bracket in s:
            if bracket in dict:
                stack.append(dict[bracket])
            else:
                if len(stack) > 0 and stack[-1] == bracket:
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False  
