import heapq
from collections import deque
from podatki import podatki, UstvariGraf

def djikstra(G, s):
    """
    Funkcija sprejme usmerjen in utežen graf G predstavljen
    s seznamom sosednosti ter začetno vozlišče s.
    Torej G[i] = [(v_1, w_1), ... (v_d, w_d)],
    kjer je (i, v_k) povezava v grafu z utežjo w_k.
    Vrne seznam razdaljeDo, ki predstavlja najkrajšo pot od vozlišča s
    do vseh ostalih.
    Vrne tudi seznam poti, ki predstavlja drevo najkrajših poti od s
    do vseh ostalih vozlišč.
    """
    n = len(G)
    
    # Nastavimo začetne vrednosti za sezname obiskani, razdaljaDo in poti.
    obiskani = [False] * n
    razdaljeDo = [-1] * n
    poti = [None] * n

    # Na vrsto dodamo trojico (d, v, p), kjer je:
    # v vozlišče, d razdalja do njega, p pa prejšnje vozlišče na najkrajši poti od
    # s do v.
    Q = [(0, s, s)]

    while Q:
        
        # Vzamemo minimalen element iz vrste
        # heapq.heappop(Q) odstrani element iz seznama  Q, ter pri tem ohranja
        # lastnost kopice : seznam Q tretira kot dvojiško drevo!
        razdalja, u, p = heapq.heappop(Q)

        # če je že obiskan, nadaljujemo.
        if obiskani[u]:
            continue
        
        # obiščemo vozlišče ter nastavimo njegovo razdaljo
        # ter predhodnika na najkrajši poti od s do u
        obiskani[u] = True
        razdaljeDo[u] = razdalja
        poti[u] = p

        # gremo čez vse sosede in dodamo potrebne elemente na vrsto.
        for (v, teza) in G[u]:
            if not obiskani[v]:

                # heap.heappush(Q, elem) doda element v seznam Q, kjer ohranja lastnost kopice.
                heapq.heappush(Q, (razdalja + teza, v, u))

    return razdaljeDo, poti



##### Primer uporabe
if __name__ == "__main__" :
    G = [[(1, 1)], [(1, 1), (3, 1)], [], [(0, 1), (1, 1), (4, 1)], [(0, 1), (1, 1), (2, 1), (3, 1)]] 

    razdalje, poti = djikstra(G, 0)
    # 
    print(razdalje, poti)

    # n = podatki()[0]
    # sez = podatki()[1]
    # G = UstvariGraf(n, sez)

    #Poiščete najkrajše razdalje od vozlišča 100 do vseh ostalih.
    #razdalje, poti = djikstra(G, 100)

    #Koliko je razdalja dG(100,100000)?

    #print(razdalje[100000])

    #Katero vozlišče je najbolj oddaljeno od vozlišča 100?

    # naj = max(razdalje)
    # indeks = razdalje.index(naj)
    # print(G[indeks][0][0])


    #Koliko vozlišč je dosegljivih iz vozlišča 100?

    print(len(poti))
