            middle = (r + l) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle - 1
        while l <= r:
        l, r = 0, len(nums) - 1
    def search(self, nums: List[int], target: int) -> int:
class Solution:
            else:
