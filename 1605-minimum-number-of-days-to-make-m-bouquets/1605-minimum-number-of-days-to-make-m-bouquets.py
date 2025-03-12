class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        N = len(bloomDay)

        if (m * k) > N:
            return -1

        def feasible(days):
            bCount = 0
            curr = 0
            for r in range(N):
                if bloomDay[r] <= days:
                    curr += 1
                    if curr == k:
                        curr = 0
                        bCount += 1
                        if bCount == m:
                            return True
                else:
                    curr = 0
            return False
            
        
        l, r = 1, max(bloomDay)
        while l < r:
            mid = l + (r-l) // 2
            if feasible(mid):
                r = mid
            else:
                l = mid + 1
        return l


        