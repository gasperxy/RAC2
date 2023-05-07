def dijkstra(G,s):
    '''Vrne najkrajšo pot od s do vseh vozlišč v grafu G'''
    n = len(G)
    D = ["inf"] * n
    P = [None] * n
    D[s] = 0     # D[i] -> razdalja od s do i
    P[s] = s
    obiskani = set()  
    q = Vrsta(V(G))  # v vrsto dodamo še nedodana vozlišča (list[range(n)])
    while len(obiskani) != n:
        c = q.popmin()  # pregledamo vsa vozlisca v q in vrnemo tistega z najmanjsim D[]
        obiskani.add(c)
        for sosed, utez in G[c]:
            if sosed not in obiskani:
                if D[c] + utez < D[sosed]:
                    D[sosed] = D[c] + utez
                    P[sosed] = c
    return D,P