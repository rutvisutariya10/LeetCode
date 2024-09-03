class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.sort()
        count = 1
        maxCount = 0
        answer = None
        for i in range(len(nums)-1): 
            if nums[i] == nums[i+1]:
                count += 1
                if count > maxCount:
                    maxCount = count
                    answer = nums[i]
            else:
                count = 1
        return answer
        
            
            
        