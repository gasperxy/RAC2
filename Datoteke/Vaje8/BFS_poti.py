def BFS_poti(G, u):
    '''Vrne najkrajše poti v neuteženem grafu G od u do vseh ostalih vozlišč.
        Graf G je predstavljen kot seznam sosedov.
    '''
    n = len(G)
    d = [0]*n  # vse razdalje na začetku nastavimo na 0
    obiskani = [False]*n
    poti = [-1] * n
    q = [(u, 0)]  # drugi element=0 je razdalja i-tega vozlišča do u
    while q:
        trenutni, razdalja = q[0]
        q = q[1:]
        if obiskani[trenutni]:
            continue
        else:
            obiskani[trenutni] = True
            d[trenutni] = razdalja
            for sosed in G[trenutni]:
                if not obiskani[sosed]:
                    # soseda dodamo na desno stran vrste
                    q += [(sosed, razdalja + 1)]
                    if poti[sosed] == -1:
                        poti[sosed] = trenutni
                       
    poti[u] = u
    return d, poti



G2_neutezen = [
    [1, 5],
    [3, 4, 5],
    [4, 5],
    [5, 2],
    [4, 5],
    [0, 1, 4]
]
print(BFS_poti(G2_neutezen, 0))



