# Case- 0 0 1 1 1 2 2 3 3
# Index 0 1 2 3 4 5 6 7 8

# class Solution {
# public:
#     int removeDuplicates(vector<int>& nums) {
#         int i =0;
#         // int ele= nums[0];
#         for(auto ele : nums)
#         {
#             if(i==0 || i==1 || nums[i-2] != ele)
#             {
#                 nums[i] = ele;
#                 i++;
#             }
#         }
#     return i ;
#     }
# };





class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l,r = 2, 2
        for r in range(2,len(nums)):
            if nums[l-2] != nums[r]:
                nums[l] = nums[r]
                l += 1
        return l
                
     
        
            
        