class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        N = len(nums)
        def next_permute(nums):
            i = N - 2
            while i >= 0 and nums[i] > nums[i+1]:
                i -= 1
            if i == -1:
                return False
            j = N - 1
            while nums[j] < nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            l, r = i+1, N-1
            while l <= r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
            return True
        
        answer.append(nums.copy())
        while True:
            if next_permute(nums):
                answer.append(nums.copy())
            else:
                return answer
            
            
            
        
#         answer = []

#         def dfs(curr):
#             if len(curr) == len(nums):
#                 answer.append(curr.copy())
#                 return
#             for i in nums:
#                 if i in curr:
#                     continue
#                 curr.append(i)
#                 dfs(curr)
#                 curr.pop()
#             return
#         dfs([])
#         return answer

            
                
            
            
            