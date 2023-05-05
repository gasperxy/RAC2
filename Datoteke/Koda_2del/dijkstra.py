def dijkstra(G,s):
    n = len(G)
    D = [inf]*n
    P = [None]*n
    D[s] = 0
    P[s] = s
    obiskani = set()
    q = vrsta(V(G))
    while len(obiskani) != n:
        c = q.popmin()
        obiskani.add(c)
        for sosed, utež in G[c]:
            if sosed not in obiskani:
                if D[c] + utež < D[sosed]:
                    D[sosed] = D[c] + utež
                    P[sosed] = c
    return D,P


def dijkstra2(G,s):
    n = len(G)
    D = [inf]*n
    P = [None]*n
    D[s] = 0
    P[s] = s
    obiskani = set()
    q = pq((0,s))
    while q:
        d,c = q.popmin()
        if c in obiskani: continue
        obiskani.add(c)
        D[c] = d
        for sosed, utež in G[c]:
            if not obiskani sosed:
                q.push(d+utež,sosed)
  