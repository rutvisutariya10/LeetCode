class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = float("inf")
        nums.sort()
        
        for k in range(len(nums)):
            l, r = 0, len(nums) - 1
            while l < r:
                if l == k:
                    l += 1
                elif r == k:
                    r -= 1
                else:
                    curr = nums[l] + nums[r] + nums[k]
                    diff = abs(target - curr)
                    if diff < abs(answer - target):
                        answer = curr
                    if curr < target:
                        l += 1
                    else:
                        r -= 1
        return answer
        