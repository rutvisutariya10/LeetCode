class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        def next_permute(nums):
            i = N - 2
            while i >= 0 and nums[i] >= nums[i+1]:
                i -= 1
            if i == -1:
                return False
            j = N - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
            l, r = i+1, N-1
            while l <= r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
            return True
        if next_permute(nums):
            return nums
        l, r = 0, N-1
        while l <= r:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
                r -= 1
        return nums