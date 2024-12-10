class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        answer = []
        nums1.sort()
        nums2.sort()
        x,y = len(nums1), len(nums2)
        i, j = 0, 0
        while i < x and j < y:
            if nums1[i] == nums2[j]:
                answer.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        
        return answer