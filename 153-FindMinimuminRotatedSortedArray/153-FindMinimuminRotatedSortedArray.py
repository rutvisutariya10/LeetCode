        [3,1,2]
        [3,4,5,6,1,2]
        """
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[r]:
                break
            middle = (l + r) // 2
            if nums[l] > nums[middle]:
                r = middle
            else:
                l = middle + 1
        [4,5,6,7,0,1,2]
        return nums[l]
        
