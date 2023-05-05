def rekonctrukcija(i,j,Pi):
    p = j
    pot = []
    while p != i:
        pot.append(p)
        p = Pi[i][p]
    pot.append(i)
    return pot.reverse()



