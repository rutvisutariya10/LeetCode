class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        m, n = 0, 0
        M, N = len(nums1), len(nums2)
        result = []
        while m < M and n < N:
            key1, val1 = nums1[m]
            key2, val2 = nums2[n]
            if  key1 < key2:
                result.append([key1, val1])
                m += 1
