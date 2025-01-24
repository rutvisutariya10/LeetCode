                g[i].append([val,j])
                g[j].append([val,i])
        
        pq = [[0,0]]
        visited = set()
        while len(visited) < len(points):
            cost, i = heapq.heappop(pq)
            if i in visited:
                continue
        answer = 0
            visited.add(i)
            answer += cost
            for nei in g[i]:
                heapq.heappush(pq,nei)
        return answer


