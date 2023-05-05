from collections import deque
import heapq
import random
from fun_naloga4 import pot
from BF_algoritem import BF

n = 300

with open("nov_graf.txt", "w") as f:
    ze = []
    for _ in range(7*n):
        od = random.randint(0, n)
        do = random.randint(0, n)
        while do == od:
            do = random.randint(0, n)
        utez = random.randint(2, 10)
        if (od, do) not in ze:
            print(f"{od} {do} {utez}", file=f)
            ze.append((od, do))
    print(len(ze))


def omrezje_novo(n):
    vse = [[] for _ in range(n+1)]
    with open('nov_graf.txt', 'r') as f:
        vrstice = f.readlines()
        veljavne = vrstice
        for vrstica in veljavne:
            trenutna = vrstica.strip().split()
            od = int(trenutna[0])
            do = int(trenutna[1])
            teza = int(trenutna[2])
            vse[od].append((do, teza))
    return vse


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


rez = omrezje_novo(n)

razdalje, poti = djikstra(rez, 0)
print("a")

raz2, pot2 = BF(rez, 0)

print(razdalje == raz2)

# for i in range(len(raz2)):
#     if raz2[i] != razdalje[i]:
#         print(i)
#         print(razdalje[i])
#         print(raz2[i])
#         print()
