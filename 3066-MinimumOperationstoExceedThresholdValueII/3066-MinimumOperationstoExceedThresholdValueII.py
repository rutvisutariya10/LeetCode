class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > 1:

        ops = 0
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            if x >= k and y >= k:
                break
            ops += 1
            newNum = min(x,y) * 2 + max(x, y)
            heapq.heappush(nums,newNum)
        return ops
        
