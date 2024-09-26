class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []

        def dfs(curr):
            if len(curr) == len(nums):
                answer.append(curr.copy())
                return
            for i in nums:
                if i in curr:
                    continue
                curr.append(i)
                dfs(curr)
                curr.pop()
            return
        dfs([])
        return answer
            
                
            
            
            