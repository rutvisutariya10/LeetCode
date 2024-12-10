class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = len(image)
        for i in range(n):
            l, r = 0, n-1
            while l <= r:
                temp = image[i][l]
                image[i][l] = abs(image[i][r] - 1)
                image[i][r] = abs(temp - 1)
                l += 1
                r -= 1
        return image
        