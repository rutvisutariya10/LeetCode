        time = [(0,k)]
        while time:
            t,node = heapq.heappop(time)
        final = 0
            for nei,wei in graph[node]:
        visited = set()
            if node in visited:
                continue
                if nei not in visited:
                    heapq.heappush(time,(wei+t,nei))
            final = max(t,final)
        
        return final if len(visited) == n else -1


            graph[u].append([v,w])
            visited.add(node)
