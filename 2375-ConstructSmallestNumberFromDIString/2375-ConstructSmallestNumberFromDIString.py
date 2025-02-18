                if idx > 0:
                    continue
                if i in used:
        def dfs(idx,st):
            for i in range(1,L+1):
        L = len(pattern) + 1
        answer = []
        used = set()
            if idx == L:
                answer.append(st)
                return True
                    if (pattern[idx-1] == 'I' and i < int(st[-1])) or (pattern[idx-1] == 'D' and i > int(st[-1])):
                        continue
                used.add(i)
                if dfs(idx+1,st+str(i)):
                    return True
                used.remove(i)
            return False

        dfs(0,"")
        return answer[0]


