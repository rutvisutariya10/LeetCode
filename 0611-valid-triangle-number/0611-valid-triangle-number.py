# x + y > z
# for each number, find two more that can satisfy this
# 1,1,3 => 1 + 3 > 1 but 1 + 1 < 2 -- handle this


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        count = 0
        l_ = len(nums)
        nums.sort()
        for i in range(2,l_):
            x = nums[i]
            l, r = 0, i - 1
            while l < r:
                y, z = nums[l], nums[r]
                if y + z > x:
                    count += (r - l)
                    r -= 1
                else:
                    l += 1
        return count
                
                
        