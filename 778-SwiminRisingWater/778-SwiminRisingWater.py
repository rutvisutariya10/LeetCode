            for dx, dy in [[x-1,y],[x+1,y],[x,y-1],[x,y+1]]:
                if dx >= 0 and dy >= 0 and dx < N and dy < N and (dx,dy) not in visited:
                    heapq.heappush(pq,(grid[dx][dy],dx,dy))
            answer = max(answer,val)
            val, x, y = heapq.heappop(pq)
        while pq:
        answer = grid[0][0]
        visited = set()
        pq = [(0,0,0)]
        N = len(grid)
    def swimInWater(self, grid: List[List[int]]) -> int:
class Solution:
        visited.add((0,0))
                    visited.add((dx,dy))
            if x == N - 1 and y == N - 1:
                break
