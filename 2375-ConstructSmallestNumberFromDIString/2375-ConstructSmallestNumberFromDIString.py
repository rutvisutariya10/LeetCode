                if idx > 0:
                    if (pattern[idx-1] == 'I' and i < int(st[-1])) or (pattern[idx-1] == 'D' and i > int(st[-1])):
                        continue
                if idx == L - 1:
                    if (pattern[idx-1] == 'I' and i > int(st[-1])) or (pattern[idx-1] == 'D' and i < int(st[-1])):
                        answer.append(st + str(i))
                        return True
                used.add(i)
                if dfs(idx+1,st+str(i)):
                    return True
                used.remove(i)
            return False

        dfs(0,"")
        return answer[0]


            
            

                    continue
