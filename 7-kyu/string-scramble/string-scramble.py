def scramble(strng, array):
    s = [0] * len(strng)
    
    for c, i in zip(strng, array):
        s[i] = c
        
    return "".join(s)