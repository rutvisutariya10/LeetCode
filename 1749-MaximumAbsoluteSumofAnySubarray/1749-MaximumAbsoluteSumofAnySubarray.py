class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        '''
        sum[i] = maxSum(nums[i:])

        relate: sum[i] = max(nums[i],nums[i]+sum[i+1],sum[i+1])

        base: sum[N] = 0

        Topo: for i in N-1 to 0

        Original: sum[0]
        '''

