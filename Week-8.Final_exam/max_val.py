def max_val(t):
    maximum = -2^32
    
    for el in t:
        if type(el) == int:
            if el >= maximum:
                maximum = el
        else:
            newmax = max_val(el)
            if newmax >= maximum:
                maximum = newmax
     
    return maximum

print(max_val((9, [3, 8, 2])))