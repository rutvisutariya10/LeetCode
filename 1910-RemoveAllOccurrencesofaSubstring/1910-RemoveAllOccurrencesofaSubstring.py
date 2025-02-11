        P = len(part)
        sl, sr, parti = 0, 0, 0
        while sr < len(s):
            elif s[sr] == part[parti]:
                if parti == 0:
                    sl = sr
                parti += 1
            elif parti != 0:
                parti = 0
                sr = sl + 1
            else:
                sr += 1
                sr += 1
            if parti == P:
                s = s[0:sl] + s[sr:]
                parti = 0
                sr = max(0,sl - P+1) 
                sl = 0
            if sr == len(s) and parti == P:
                s = s[0:sl]
        return s


