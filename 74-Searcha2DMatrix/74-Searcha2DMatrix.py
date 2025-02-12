            if matrix[middle][N-1] < target:
                l = middle + 1
            else:
                r = middle - 1
        if targetRow == -1:
            return False
        l, r = 0, N - 1
        while l <= r:
            middle = (l + r) // 2
            if matrix[targetRow][middle] == target:
                return True
            if matrix[targetRow][middle] < target:
                l = middle + 1
            else:
                r = middle - 1
        return False
        
