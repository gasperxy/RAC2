def BFS_s_t(G, u, t):
    '''Vrne najkrajše poti v neuteženem grafu G od u do do vozlišča t.
        Graf G je predstavljen kot seznam sosedov.
    '''
    n = len(G)
    if u == t:
        return 0, []
    obiskani = [False]*n
    pot = list()
    vrsta = [(u, 0, u)]  # tu hranimo vsa vozlišča in njihove starše
    q = [(u, 0, u)]  # drugi element=0 je razdalja i-tega vozlišča do u
    while q:
        trenutni, razdalja, stars = q[0]
        q = q[1:]
        if obiskani[trenutni]:
            continue
        else:
            obiskani[trenutni] = True
            for sosed in G[trenutni]:
                if sosed == t and razdalja == 0:
                    # direktni sosed
                    return 1, [sosed, u]
                if sosed == t:
                    pot.append(t)
                    pot.append(trenutni)
                    while True:
                        for elt in vrsta:
                            if elt[0] == trenutni:
                                stars = elt[2]
                                if stars == u:
                                    pot.append(u)
                                    return razdalja + 1, pot
                                pot.append(stars)
                                trenutni = stars
                
                if not obiskani[sosed]:
                    # soseda dodamo na desno stran vrste
                    q += [(sosed, razdalja + 1, trenutni)]
                    vrsta += [(sosed, razdalja, trenutni)]


G2_neutezen = [
    [1, 5],
    [3, 4, 5],
    [4, 5],
    [5, 2],
    [4, 5],
    [0, 1, 4]
]

print(BFS_s_t(G2_neutezen, 0, 1))
print(BFS_s_t(G2_neutezen, 0, 2))
print(BFS_s_t(G2_neutezen, 5, 3))
print(BFS_s_t(G2_neutezen, 0, 0))

