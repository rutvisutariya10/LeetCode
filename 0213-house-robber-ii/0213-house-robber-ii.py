class Solution:
    def rob(self, nums: List[int]) -> int:
        L = len(nums)
        if L == 1:
            return nums[0]
        M = [0] * (L+2)
        N = [0] * (L+2)
        for i in range(L-1,0,-1):
            M[i] = max(M[i+1],nums[i]+M[i+2])
        for i in range(L-2,-1,-1):
            N[i] = max(N[i+1],nums[i]+N[i+2])
        return max(M[1],N[0])
        