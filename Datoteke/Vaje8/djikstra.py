import heapq  # kopica
from collections import deque
from rac2_vaje8 import *
from BFS_poti import BFS_poti
from pot_s_t import pot_s_t

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
    poti = [-1] * n
    # Na vrsto dodamo trojico (d, v, p), kjer je:
    # v vozlišče, d razdalja do njega, p pa prejšnje vozlišče na najkrajši poti od
    # s do v.
    Q = [(0, s, s)]

    while Q:
        
        # Vzamemo minimalen element iz vrste
        # heapq.heappop(Q) odstrani element iz seznama  Q, ter pri tem ohranja
        # lastnost kopice : seznam Q tretira kot dvojiško drevo!
        razdalja, u, p = heapq.heappop(Q)  # iz seznama q vzame zadnji element, ampak ohranja lastnosti kopice

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

def pot(drevo, s, t):
    sez_pot = list()  # tu hranimo vse do sedaj pregledane starše vozlišč
    # sprehajamo se od končnega vozlišča t do s
    stars = drevo[t]  # starš od vozlišča t
    sez_pot.append(t)
    sez_pot.append(stars)
    while stars != s:
        # ponavljamo, dokler ne pridemo do starša enakega vozlišču s
        stars = drevo[stars]
        sez_pot.append(stars)
    return sez_pot



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

G2_neutezen = [
    [1, 5],
    [3, 4, 5],
    [4, 5],
    [5, 2],
    [4, 5],
    [0, 1, 4]
]

G4 = [[(1,1), (3,1)], [(2,1)], [(0,1), (3,1)], [(1,1)]]

G3 = [
    [(3,1), (2,1)],
    [(0,1), (2,1), (4,1)],
    [(3,1)],
    [(1,1), (4,1)],
    [(0,1), (2,1)]
]

tab = seznam_povezav('roadNet-TX.txt')
graf2 = ustvari_graf(tab)
razdalje, poti = djikstra(graf2, 100)

#graf_neutezen = ustvari_neutezen_graf(tab)
#razdalje2, poti2 = BFS_poti(graf_neutezen, 100)

#razdalje, poti = djikstra(G2, 0)
najkrajsa_pot = pot(poti, 100, 100000)
print(najkrajsa_pot)
print(razdalje[100000], len(najkrajsa_pot))




