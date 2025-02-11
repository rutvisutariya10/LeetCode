            if height[l] <= height[r]:
                currStored = 0
                s = l
                while l < r:
                    currStored += height[s] - height[l]
                    l += 1
                waterStored += currStored 
            r += 1
        waterStored = 0
        while r < H:
            r += 1
        left = l
        l,r = H - 1, H - 1
        return waterStored


            
             

        
