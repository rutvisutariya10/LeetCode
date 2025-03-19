class Solution:
    def minOperations(self, nums: List[int]) -> int:
        N = len(nums)
        count = 0
        for i in range(N-2):
            if nums[i] == 0:
                nums[i] ^= 1
                nums[i+1] ^= 1
                nums[i+2] ^= 1
                count += 1
        if sum(nums) == N:
            return count
        return -1
            
            



        