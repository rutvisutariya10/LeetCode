class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        climb = [0] * l
        climb[l-1] = cost[l-1]
        climb[l-2] = cost[l-2]
        for i in range(len(cost) - 3, -1, -1):
            climb[i] = cost[i] + min(climb[i+1],climb[i+2])
        return min(climb[0],climb[1])