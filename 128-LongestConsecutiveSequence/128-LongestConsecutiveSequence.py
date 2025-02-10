class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
            
        numSet = set(nums)
        longest = 0
        for num in numSet:
            if num - 1 in numSet:
                continue
            while num + 1 in numSet:
            currMax = 1
                currMax += 1
                num += 1
            longest = max(longest, currMax)
        return longest

