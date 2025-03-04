class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Either I rob a house or I don't
        If there is only one house, I rob it
        2 houses, max of 2
        3 houses is where 
        Subprobs- M[i] = Max money I can rob reaching ith house
        Relate- M[i] = max(nums[i]+M[i+2],M[i+1])
        Topology- n >= i > =0
        Base- M[n+1] = 0 = M[n]
        Original- M[0]
        '''
        L = len(nums)
        M = [0] * (L+2)
        for i in range(L-1,-1,-1):
            M[i] = max(M[i+1],nums[i]+M[i+2])
        return M[0]