            if len(kfreq) < k:
                kfreq.append((c,num))
                continue
                kfreq.sort(reverse=True)
            if kfreq[-1][0] < c:
                kfreq.pop()
                kfreq.append((c,num))
        return [i for c,i in kfreq]
            
                kfreq.sort(reverse=True)
        
