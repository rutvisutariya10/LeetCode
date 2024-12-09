class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 0,0
        while r < len(nums):
            if l != r and nums[l] == nums[r]:
                nums.remove(nums[r])
            else:
                l = r
                r += 1
        return len(nums)
        
            
        