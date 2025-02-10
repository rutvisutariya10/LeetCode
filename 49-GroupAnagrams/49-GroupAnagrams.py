            if i in used:
                continue
            ana = [strs[i]]
            used.add(i)
        for i in range(len(strs)):
        answer = []
        used = set()
            ht.append(h)
                h[c] = h.get(c, 0) + 1
            for c in s:
            h = {}
            for j in range(i+1,len(strs)):
                if ht[i] == ht[j] and j not in used:
                    ana.append(strs[j])
                    used.add(j)
            answer.append(ana)
        return answer
                


