class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        maxWater - maintain this
        '''
        maybe look from both sides? because area = l * b
        so farther is better and higher is better
        now if height of left is > height of right - move right else move left
        update max
        while l < r:
        l, r = 0, len(height) - 1

        maxWater = 0
            maxWater = max(maxWater,currWater)
            currWater = (r-l) * min(height[l],height[r])
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxWater
        
