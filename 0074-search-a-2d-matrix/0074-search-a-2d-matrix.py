class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        find the row where it might be present.
        minimum k s.t. m[k][0] >= target

        m[k][0] > target -> right = middle
        m[k][0] = target -> right = middle
        m[k][0] < target -> left = middle + 1
        '''
        M, N = len(matrix), len(matrix[0])
        l, r = 0, M-1
        while l <= r:
            m = l + (r-l) // 2
            if matrix[m][0] == target:
                return True
            if matrix[m][0] > target:
                r = m - 1
            else:
                l = m + 1
        row = l - 1
        l, r = 0, N-1
        while l <= r:
            m = l + (r-l) // 2
            if matrix[row][m] == target:
                return True
            if matrix[row][m] > target:
                r = m - 1
            else:
                l = m + 1
        return False
        