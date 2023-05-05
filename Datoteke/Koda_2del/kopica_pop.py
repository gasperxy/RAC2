def pop(T):
    '''odstrani prvi element iz kopice'''
    koren = T[1]
    T[1] = T[-1]
    T.pop()
    levi_sin = 2*i
    desni_sin = 2*i+1
    while T[i] > T[levi_sin] or T[i] > T[desni_sin]:
        if T[levi_sin] > T[desni_sin]:
            T[i],T[desni_sin] = T[desni_sin],T[i]
            i = desni_sin
            levi_sin = 2*i
            desni_sin = 2*i+1
        else:
            T[i],T[levi_sin] = T[levi_sin],T[i]
            i = levi_sin
            levi_sin = 2*i
            desni_sin = 2*i+1
    return koren