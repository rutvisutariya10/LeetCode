            return True
        used = set()
        answer = []
        for i in range(len(strs)):
            if i in used:
                continue
            ana = [strs[i]]
            for j in range(i+1,len(strs)):
                if isAnagram(ht[i],ht[j]) and j not in used:
                    ana.append(strs[j])
                    used.add(j)
            answer.append(ana)
            used.add(i)
        return answer
                



        
