        currMin = 1
        l, r = 1, max(piles)
        while l <= r:
            middle = (l + r) // 2
            hours = 0
            for bananas in piles:
                hours += (bananas//middle)  
                if bananas % middle != 0:
                    hours += 1
            if h < hours:
                l = middle + 1
            else:
                r = middle - 1
                currMin = middle
        return currMin

        
