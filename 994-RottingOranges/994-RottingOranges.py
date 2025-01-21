                if new_c >= 0 and new_r >= 0 and new_c < N and new_r < M and grid[new_r][new_c] == 1:
                    grid[new_r][new_c] = 2
                    fresh -= 1
                    queue.append((new_r,new_c,time+1))
                    max_time = max(max_time, time + 1)
        if fresh > 0:
            return -1
                new_c = c + dc
                new_r = r + dr
            for dr,dc in directions:
            directions = [(-1,0),(1,0),(0,-1),(0,1)]
            r, c, time = queue.popleft()
        while queue:
        return max_time
        


