        pop when you see something smaller.
        '''
        stack = []
        maxArea = 0
        for i,height in enumerate(heights):
            l = i
            while stack and stack[-1][0] > height:
                eleHeight, eleReach = stack.pop()
                currArea = (i - eleReach) * eleHeight
                l = eleReach
                maxArea = max(currArea,maxArea)
            stack.append((height,l))
        stackLen = len(heights)
        for height,reach in stack:
            newArea = (stackLen - reach) * height
            print(newArea)
            maxArea = max(newArea,maxArea)
