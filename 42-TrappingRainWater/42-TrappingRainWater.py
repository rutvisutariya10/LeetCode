        #         waterStored += currStored 
        #     r += 1
        # left = l
        # l,r = H - 1, H - 1
        # return waterStored

        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        waterStored = 0
        while l < r:
            if l_max < r_max:
                l += 1
                waterStored += l_max - height[l]
            else:
                r -= 1
                waterStored += r_max - height[r]
        return waterStored


            
                l_max = max(height[l],l_max)
             
                r_max = max(height[r],r_max)
