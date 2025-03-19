class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        count = 0
        for i in range(N-2):
            if nums[i] == 0:
                for j in range(i,i+3):
                    nums[j] = 1 - nums[j]
                count += 1
        if sum(nums) == N:
            return count
        return -1
            
            



        