from collections import deque

def bfs(G, s):
    """
    Funkcija sprejme graf G predstavljen
    s seznamom sosednosti ter začetno vozlišče s.
    Torej G[i] = [(v_1, w_1), ... (v_d, w_d)],
    kjer je (i, v_k) povezava v grafu z utežjo w_k.
    Vrne seznam razdaljeDo, ki predstavlja najkrajšo pot od vozlišča s
    do vseh ostalih.
    Vrne tudi seznam poti, ki predstavlja drevo najkrajših poti od s
    do vseh ostalih vozlišč.
    """
    n = len(G)
    razdalje = [-1] * n
    #vsak el poti[v] predstavlja starsa v-ja na najkrajsi poti od s do v
    poti = [-1] * n    #poti od s do vseh ostalih vozlisc
    razdalje[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        # teze ne uposteamo 
        for v, _ in G[u]:   # poglej sosednje vozlisce (v),tezo ignoriraj
            if razdalje[v] == -1:
                razdalje[v] = razdalje[u] + 1
                poti[v] = u
                q.append(v)
    return razdalje, poti


G = [
    [(1,1.5), (5,2)],
    [(3, 1), (4, 1.2), (5, 0.3)],
    [(4,1), (5, 0.8)],
    [(5,1), (2, 1.5)],
    [(4,1), (5, 0.8)],
    [(0, 1), (1,0.5), (4, 2)]
]

razdalje, poti = bfs(G, 0)

print(razdalje, poti)



from collections import deque

def bfs_modificiran(G, s, t):
    """
    Funkcija sprejme graf G predstavljen
    s seznamom sosednosti ter začetno vozlišče s in končno vozlišče t.
    Torej G[i] = [(v_1, w_1), ... (v_d, w_d)],
    kjer je (i, v_k) povezava v grafu z utežjo w_k.
    Vrne razdaljo med vozliščema s in t v grafu ter pot (kot drevo) med njima.
    """
    n = len(G)
    razdalje = [-1] * n
    # vsak el. poti[v] predstavlja starsa v-ja na najkrajsi poti od s do v
    poti = [-1] * n    # poti od s do vseh ostalih vozlisc
    razdalje[s] = 0
    q = deque([s])
    while q:
        u = q.popleft()
        if u == t:
            break
        # teze ne uposteamo 
        for v, _ in G[u]:   # poglej sosednje vozlisce (v),tezo ignoriraj
            if razdalje[v] == -1:
                razdalje[v] = razdalje[u] + 1
                poti[v] = u
                q.append(v)
    if razdalje[t] == -1:
        return None, None
    # Sestavimo pot od t do s glede na starše, ki jih beležimo v seznamu poti
    pot = [t]
    while pot[-1] != s:
        pot.append(poti[pot[-1]])
    pot.reverse()
    return razdalje[t], pot
