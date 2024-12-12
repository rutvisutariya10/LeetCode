class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        size = len(nums)
        l = 0
        r = size - 1
        while l < r and (nums[l] <= nums[l+1] or nums[r-1] <= nums[r]):
            if nums[l] <= nums[l+1]:
                l += 1
            if nums[r-1] <= nums[r]:
                r -= 1            
        
        if l >= r:
            return 0
        
        max_ = max(nums[l:r+1])
        min_ = min(nums[l:r+1])
        
        while l > 0 and nums[l-1] > min_:
            l -= 1
        while r < size - 1 and nums[r+1] < max_:
            r += 1
        
        
        return r - l + 1
                
        