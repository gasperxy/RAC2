def push(T,x):
    '''doda element x v kopico T'''
    T.append(x)
    i = len(T)-1
    oče = i//2
    while T[oče] > T[i]:
        T[oče],T[i]=T[i],T[oče]
        i = oče
        oče = i//2