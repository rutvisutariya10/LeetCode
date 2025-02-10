        ''' 
        Sort each word and add it to the dictionary corresponding to the sorted word
        '''
        ht = collections.defaultdict(list)
        for s in strs:
            ht[''.join(sorted(s))].append(s)
        return list(ht.values())
                



        
