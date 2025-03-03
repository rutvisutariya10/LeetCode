        [1,2,4,3]
        '''
        L = len(nums)
        less,more,p = [],[],[]

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        '''
        [1,3,4,2]
        
        for i in range(L):
            if nums[i] < pivot:
                less.append(nums[i])
            elif nums[i] > pivot:
                more.append(nums[i])
            else:
                p.append(nums[i])
        return less+p+more

