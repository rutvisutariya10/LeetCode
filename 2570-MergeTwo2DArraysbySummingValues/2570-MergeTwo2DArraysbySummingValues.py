                result.append([key1, val1])
                m += 1
            elif key1 > key2:
                result.append([key2,val2])
                n += 1
            else:
                result.append([key1, val1+val2])
                m += 1
                n += 1
        while m < M:
            key1, val1 = nums1[m]
            result.append([key1, val1])
            m += 1
        while n < N:
            key2, val2 = nums2[n]
            result.append([key2,val2])
            n += 1
        return result
        
        
