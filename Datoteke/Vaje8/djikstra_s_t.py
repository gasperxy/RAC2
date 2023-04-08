import heapq  # kopica
from collections import deque

def djikstra(G, s, t):
    '''
        Funkcija sprejme usmerjen in utežen graf G predstavljen
        s seznamom sosednosti ter začetno vozlišče s.
        Torej G[i] = [(v_1, w_1), ... (v_d, w_d)],
        kjer je (i, v_k) povezava v grafu z utežjo w_k.
        Vrne razdaljo najkrajše poti od vozlišča s
        do vozlišča t. Vrne tudi pot od s do vozlišča t.
    '''
    if s == t:
        return 0, []
    
    n = len(G)
    # Nastavimo začetne vrednosti za sezname obiskani, razdaljaDo in poti.
    obiskani = [False] * n
    pot = list()
    vrsta = [(s, 0, s)]
    # Na vrsto dodamo trojico (d, v, p), kjer je:
    # v vozlišče, d razdalja do njega, p pa prejšnje vozlišče na najkrajši poti od
    # s do v.
    Q = [(0, s, s)]

    while Q:
        # Vzamemo minimalen element iz vrste
        # heapq.heappop(Q) odstrani element iz seznama  Q, ter pri tem ohranja
        # lastnost kopice : seznam Q tretira kot dvojiško drevo!
        razdalja, u, p = heapq.heappop(Q)  # iz seznama q vzame zadnji element, ampak ohranja lastnosti kopice

        if obiskani[u]:
            continue
        obiskani[u] = True        

        # gremo čez vse sosede in dodamo potrebne elemente na vrsto.
        for (v, teza) in G[u]:
            if v == t and razdalja == 0:
                # direktni sosed
                return 1, [v, s]
            
            if v == t:
                pot.append(t)
                pot.append(u)
                while True:
                    for elt in vrsta:
                        if elt[0] == u:
                            stars = elt[2]
                            if stars == s:
                                pot.append(s)
                                return razdalja + 1, pot
                            pot.append(stars)
                            u = stars
            
            if not obiskani[v]:
                # heap.heappush(Q, elem) doda element v seznam Q, kjer ohranja lastnost kopice.
                heapq.heappush(Q, (razdalja + teza, v, u))
                vrsta += [(v, razdalja, u)]



##### Primer uporabe

G = [
    [(1,1.5), (5,2)],
    [(3, 1), (4, 1.2), (5, 0.3)],
    [(4,1), (5, 0.8)],
    [(5,1), (2, 1.5)],
    [(4,1), (5, 0.8)],
    [(0, 1), (1,0.5), (4, 2)]
]

G2 = [
    [(1,1), (5,1)],
    [(3, 1), (4, 1), (5, 1)],
    [(4,1), (5, 1)],
    [(5,1), (2, 1)],
    [(4,1), (5, 1)],
    [(0, 1), (1,1), (4, 1)]
]

print(djikstra(G2, 0, 1))
print(djikstra(G2, 0, 2))
print(djikstra(G2, 5, 3))
print(djikstra(G2, 0, 0))


