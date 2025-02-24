                    l = dfs(e)
                    if l:
                        return [curr] + l


        # first move bob, and track visited times
        bob_path = dfs(bob)
        bob_visited_times = {}
        for i, v in enumerate(bob_path):
            bob_visited_times[v] = i

        visited = set()
        def dfs_alice(curr, visit_time):
            max_amount = float('-inf')
            visited.add(curr)
            for e in graph[curr]:
                if e not in visited:
                    max_amount = max(max_amount, dfs_alice(e, visit_time + 1))

            vertex_income = amount[curr]
            if curr in bob_visited_times and bob_visited_times[curr] < visit_time:
                vertex_income = 0
            elif curr in bob_visited_times and bob_visited_times[curr] == visit_time:
                vertex_income = amount[curr] // 2
            if max_amount == float('-inf'):
