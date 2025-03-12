class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        smallest k such that nums[k] 

        if nums[middle] > target -> not on the right -> update right. right = middle or middle - 1?
        if nums[middle] == target -> maybe this is the answer -> or answer on the left. right = middle? or middle - 1?
        if nums[middle] < target -> answer on the right -> left = middle or middle + 1

        so if i choose >= ans say right might have the target.let left come to it while checking it's side.we might find something even smaller.
        1,3,4

        '''
        N = len(nums)
        l, r = 0, N - 1
        while l < r:
            middle = l + (r-l) // 2
            if nums[middle] >= target:
                r = middle
            else:
                l = middle + 1
        if l < N and nums[l] == target:
            return l 
        return -1