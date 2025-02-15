
        0 -> 1 -> 2 -> 3 -> 4
                  A         | 
                  |---------|
        '''
        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow] 
            fast = nums[nums[fast]] 
            if slow == fast:
                break
        [1,2,3,4,2]
        finder = nums[0]
        while slow != finder:
            slow = nums[slow]
            finder = nums[finder]
        return finder
        
        
