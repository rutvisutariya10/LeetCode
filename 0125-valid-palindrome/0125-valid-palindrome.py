class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        new_string = ""
        for i in s:
            if i.isalpha():
                new_string += i.lower()
            elif i in "0123456789":
                new_string += i
        left = 0
        right = len(new_string) - 1
        while left < right:
            if new_string[left] == new_string[right]:
                left += 1
                right -= 1
                continue
            return False
        return True
        