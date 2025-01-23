            for nei in preq[i]:
            visited.add(i)
                if not dfs(nei):
                    return False
            visited.remove(i)
            preq[i] = []
            answer.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return answer
