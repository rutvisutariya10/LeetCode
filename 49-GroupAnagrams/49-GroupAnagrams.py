                return False
            if sum(x.values()) != sum(y.values()):
            for i in x.keys():
                if i not in y or x[i] != y[i]:
                    return False
            return True
        used = set()
        answer = []
        for i in range(len(strs)):
            if strs[i] in used:
                continue
            ana = [strs[i]]
            for j in range(i+1,len(strs)):
                if isAnagram(ht[strs[i]],ht[strs[j]]) and strs[j] not in used:
                    ana.append(strs[j])
                    used.add(strs[j])
            answer.append(ana)
        return answer
                

