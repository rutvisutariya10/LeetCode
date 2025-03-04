class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        either prefix or suffix
        SRTBOT
        Subproblems- S(i) = the ith step
        Relation- S(i) = cost[i] + min(S[i+1],S[i+2])
        Topology- for n >= i >=0
        Base- S(n) = 0, S(n+1) = 0
        Original- S(0)
        Time- O(n)
        '''
        L = len(cost)
        S = [0] * (L + 2)
        for i in range(L-1,-1,-1):
            S[i] = cost[i] + min(S[i+1],S[i+2])
        return min(S[0],S[1])