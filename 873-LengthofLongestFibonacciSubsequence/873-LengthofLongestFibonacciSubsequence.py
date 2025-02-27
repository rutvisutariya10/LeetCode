        L = len(arr)
        '''
        [1,2,3,5,8] => find 13 (not found) => update longest_yet
        Because 13 not found, remove all except the first element 
        and repeat the process with
        [1,3] => find 4
        [1,3,4] => find 7
        [1,3,4,7] => find 11 (not found) => update longest yet
        longest_yet = 0
        for i in range(L):
        check = set(arr)
            for j in range(i+1,L):
                while (x+y) in check:
                count = 0
                x, y = arr[i], arr[j]
                    count += 1
                    x, y = y, x+y 
                if count > 0:
                    longest_yet = max(longest_yet,count+2)
        return longest_yet

