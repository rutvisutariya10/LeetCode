        count = collections.defaultdict(int)
        L= len(nums)
        for i in range(L-k+1):
            temp_count = set()
            temp_count.add(nums[i])
            for j in range(i+1,i+k):
                temp_count.add(nums[j])
            for key in temp_count:
                count[key] += 1
        max_number = -1
        for key,value in count.items():
            if value == 1:
                max_number = max(key,max_number)
        return max_number
                
