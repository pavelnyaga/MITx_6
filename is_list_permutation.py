def is_list_permutation(L1, L2):
    if len(L1) == len(L2) and len(L1) != 0:

        freq1 = {}
        freq2 = {}
        
        for k in L1:
            if k not in freq1:
                freq1[k] = 1
            else:
                freq1[k] += 1
        
        for k in L2:
            if k in freq1:
                if k not in freq2:
                    freq2[k] = 1
                else:
                    freq2[k] += 1
            else:
                return False 
                
        for k in freq1:
            if freq1[k] != freq2[k]:
                return False
        
        m = 0
        mx = 0
        
        for x in freq2:
            if freq2[x] > m:
                m = freq2[x]
                mx = x
        
        return (mx, m, type(mx))
        
    elif len (L1) == 0 and len(L2) == 0:
        return (None, None, None)
    else:
        return False

print (is_list_permutation([1, 2, 1], [2, 1, 2]))