        for i,n in enumerate(nums):
        h = collections.defaultdict(list)
        # Count the occurence of each element?

            h[n].append(i)
        for k in h.keys():
            needed = target - k
            if needed == k:
                    return [h[k][0], h[k][1]]
            elif needed in h:
                return [h[k][0],h[needed][0]]

        print(h)
                if len(h[k]) > 1:
            
