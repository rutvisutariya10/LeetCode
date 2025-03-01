class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        l,r = 0,0
        while r < N:
            if nums[r] != 0:
                nums[l] = nums[r]
                l += 1
            r += 1
        while l < N:
            nums[l] = 0
        return nums
            l += 1
        
