class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            summation = numbers[left] + numbers[right]
            if summation == target:
                return [left+1,right+1]
            elif summation < target:
                left += 1
            else:
                right -= 1
        