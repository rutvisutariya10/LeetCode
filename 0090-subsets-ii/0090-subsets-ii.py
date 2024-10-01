class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        curr = []
        def dfs(idx):
            if idx == len(nums):
                answer.append(curr.copy())
                return
            curr.append(nums[idx])
            dfs(idx+1)
            curr.pop()
            while idx < len(nums) - 1 and nums[idx] == nums[idx+1]:
                idx += 1
            dfs(idx+1)
        
        dfs(0)
        return answer
                