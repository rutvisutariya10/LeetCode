class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        '''
        [-1,-1,0,1]
        mid = 1
        [-3,-2,-1,0,0,1,2]
        '''
        N = len(nums)
        low, high = 0, N-1

        # Counting Negatives
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] >= 0:
                high = mid - 1
            else:
                low = mid + 1
        neg = low

        '''
        [-1,-1,0,1]
        mid = 1
        '''

        # Counting Positives
        low, high = 0, N-1
        while low <= high:
            mid = (low+high) // 2
            if nums[mid] <= 0:
                low = mid + 1
            else:
                high = mid - 1
        pos = N - low

        return max(neg,pos)
