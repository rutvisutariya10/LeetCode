class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        '''

        '''
        l, longest, N = 0, 0, len(nums)
        for r in range(N):
            curr = 1
            x = nums[r]
            for i in range(r-1,l-1,-1):
                y = nums[i]
                if x & y == 0:
                    curr += 1
                else:
                    l = i + 1
                    break
            longest = max(longest,curr)
        return longest

