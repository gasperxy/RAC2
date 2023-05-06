import heapq
from collections import deque

def djikstra_modificiran(G, s, t):
    """
    Funkcija sprejme usmerjen in utežen graf G predstavljen
    s seznamom sosednosti ter začetno vozlišče s.
    Torej G[i] = [(v_1, w_1), ... (v_d, w_d)],
    kjer je (i, v_k) povezava v grafu z utežjo w_k.
    Vrne seznam razdaljeDo, ki predstavlja najkrajšo pot od vozlišča s
    do vseh ostalih.
    Vrne tudi seznam poti, ki predstavlja drevo najkrajših poti od s
    do vseh ostalih vozlišč.
    Poleg tega sprejme tudi končno vozlišče t in vrne najcenejšo razdaljo
    od s do t. Prav tako vrne drevo najkraših poti kot seznam, kjer
    je i-ti element oče vozlišča i-1.
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
        # heapq.heappop(Q) odstrani element iz seznama Q, ter pri tem ohranja
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

        # če smo prišli do vozlišča s, skonstruiramo drevo poti
        # in vrnemo najcenejšo razdaljo od s do t
        if u == t:
            pot_do_t = [t]
            pred = poti[t]
            while pred != s:
                pot_do_t.append(pred)
                pred = poti[pred]
            pot_do_t.append(s)
            return razdaljeDo[t], pot_do_t
        
        # gremo čez vse sosede in dodamo potrebne elemente na vrsto.
        for (v, teza) in G[u]:
            if not obiskani[v]:

                # heap.heappush(Q, elem) doda element v seznam Q, kjer ohranja lastnost kopice.
                heapq.heappush(Q, (razdalja + teza, v, u))

    return razdaljeDo, poti

def BFS_modificiran(G, s, t):
    """
    BFS vrne najkrajše poti od s do vseh ostalih vozlišč. Tu je s štartno 
    vozlišče, G pa je graf, ki je podan kot seznam sosednosti. Seznam d 
    predstavlja najkrajšo pot od vozlišča s do vseh ostalih. Poleg tega 
    sprejme tudi končno vozlišče t in vrne najcenejšo razdaljo
    od s do t. Prav tako vrne drevo najkraših poti kot seznam, kjer
    je i-ti element oče vozlišča i-1.
    """
    n = len(G)

    # Nastavimo začetne vrednosti za sezname d, obiskani, in poti.
    d = [0] * n  
    obiskani = [False] * n
    poti = [-1] * n

    # Na vrsto dodamo trojico (v, d, p), kjer je: v vozlišče, d je razdalja, p 
    # pa prejšnje vozlišče na najkrajši poti od u do v.
    q = deque([(s, 0, s)])

    while q:
        u, razdalja, p = q.popleft()

        if obiskani[u]: 
            continue # smo ga že obiskali
        
        # obiščemo vozlišče ter nastavimo njegovo razdaljo
        # ter predhodnika na najkrajši poti od s do u
        obiskani[u] = True
        d[u] = razdalja
        poti[u] = p

        # če smo prišli do vozlišča s, skonstruiramo drevo poti
        # in vrnemo najcenejšo razdaljo od s do t
        if u == t:
            pot_do_t = [t]
            pred = poti[t]
            while pred != s:
                pot_do_t.append(pred)
                pred = poti[pred]
            pot_do_t.append(s)
            return d[t], pot_do_t

        # gremo čez vse sosede in dodamo potrebne elemente na vrsto.
        for sosed in G[u]:
            if not obiskani[sosed]:
                q.append((sosed, razdalja + 1, u)) #doda nov element v q
    return d, poti


if __name__=="__main__":

    G = [
    [(1,1.5), (5,2)],
    [(3, 1), (4, 1.2), (5, 0.3)],
    [(4,1), (5, 0.8)],
    [(5,1), (2, 1.5)],
    [(4,1), (5, 0.8)],
    [(0, 1), (1,0.5), (4, 2)]
    ]

    F = [
        [1, 5],
        [3, 4, 5],
        [4, 5],
        [5, 2],
        [4, 5],
        [0, 1, 4]
    ]

    # razdalje, poti = djikstra_modificiran(G, 0, 3)
    # print(razdalje)
    # print(poti)

    # razdalje, poti = BFS_modificiran(F, 0, 3)
    # print(razdalje)
    # print(poti)