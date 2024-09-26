class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(idx,currSum,l):
            if currSum == target:
                res.append(l.copy())
                return
            if idx >= len(candidates) or currSum > target:
                return
            l.append(candidates[idx])
            dfs(idx,currSum+candidates[idx],l)
            l.pop()
            dfs(idx + 1,currSum,l)
        dfs(0,0,[])
        return res
            



            
