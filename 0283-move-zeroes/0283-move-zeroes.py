class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
       
        i,j = 0,0 
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            elif i != j:
                nums[i] = nums[j]
                nums[j] = 0
                i += 1
            else:
                i += 1
                j += 1
                
                
            
            
        