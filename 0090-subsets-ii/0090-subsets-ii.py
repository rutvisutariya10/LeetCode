class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()
        def dfs(i,curr):
            if i >= len(nums):
                if tuple(curr) not in answer:
                    answer.add(tuple(curr.copy()))
                return
            curr.append(nums[i])
            dfs(i+1,curr)
            curr.pop()
            dfs(i+1,curr)
        
        dfs(0,[])
        
        return list(answer)
                    