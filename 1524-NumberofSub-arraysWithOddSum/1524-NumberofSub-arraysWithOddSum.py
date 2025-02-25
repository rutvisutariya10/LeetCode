
            

        
        
        for a in arr:
            s += a
            if s % 2 == 0:
                r = (r + o) % MOD
                e += 1
            else:
                r = (r + e) % MOD
                o += 1
                
        return r
