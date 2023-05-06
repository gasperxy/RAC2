from merilnik.py import *
import heapq  # kopica
from collections import deque
# from rac2_vaje8 import razberiGraf

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

def djikstra_druga(G, s, t):
    '''Funkcija, ki vrne razdaljo med s in t v grafu G ter pot (kot drevo) med njima.'''
    n = len(G)
    obiskani = [False] * n
    razdaljeDo = [-1] * n
    poti = [None] * n
    Q = [(0, s, s)]
    while Q:
        razdalja, u, p = heapq.heappop(Q)  
        if obiskani[u]:
            continue
        obiskani[u] = True
        razdaljeDo[u] = razdalja
        poti[u] = p
        if u == t:
            break
        for (v, teza) in G[u]:
            if not obiskani[v]:
                heapq.heappush(Q, (razdalja + teza, v, u))
    return razdaljeDo, poti



def datoteka(ime):
    '''Funkcija, ki spremeni datoteko txt v seznam parov vozlišč.'''
    seznam = list()
    with open(ime, 'r') as file:
        vse_vrst = file.readlines()
        vrstice = vse_vrst[4:]
        for i in vrstice:
            i = i[:-1]
            od = int(i.split('\t')[0])
            do = int(i.split('\t')[1])
            seznam.append((od, do))
        seznam.sort(key=lambda a: a[0])
    return seznam



def seznam_sosednosti(seznam):
    '''Funkcija, ki spremeni seznam parov sosednjih vozlišč v seznam sosednosti z utežjo 1.'''
    matrika = [list() for _ in range(seznam[-1][0] + 1)] # toliko je vseh vozlišč
    for i,j in seznam:
        matrika[i].append((j,1))
    return matrika



primer1 = datoteka("roadNet-TX.txt")
graf = seznam_sosednosti(primer1)
najkrajse_razdalje_od_sto2, poti = djikstra_druga(graf, 100,100000)
print(najkrajse_razdalje_od_sto2)




primer1 = datoteka("roadNet-TX.txt")
graf = seznam_sosednosti(primer1)
najkrajse_razdalje_od_sto, poti = djikstra(graf, 100)
print(najkrajse_razdalje_od_sto)
# razdalja dG(100,100000)
dG = najkrajse_razdalje_od_sto[100000]
print(dG)
# Katero vozlišče je najbolj oddaljeno od vozlišča 100
najvecja_razdalja = max(najkrajse_razdalje_od_sto)
ind = najkrajse_razdalje_od_sto.index(najvecja_razdalja)
print(ind)
# Koliko vozlišč je dosegljivih iz vozlišča 100?
def koliko_vozlisc(seznam):
    stevec = 0
    for i in seznam:
        if i >= 1:
            stevec += 1
    return stevec

print(koliko_vozlisc(najkrajse_razdalje_od_sto))












def izmeri_cas(fun, primer):
    """Izmeri čas izvajanja funkcije `fun` pri argumentu `primer`."""
    cas1 = time.perf_counter()
    fun(primer)
    cas2 = time.perf_counter()
    cas = cas2 - cas1
    return cas




izmeri_cas(





















##### Primer uporabe

# G1 = [
#     [(1,1.5), (5,2)],
#     [(3, 1), (4, 1.2), (5, 0.3)],
#     [(4,1), (5, 0.8)],
#     [(5,1), (2, 1.5)],
#     [(4,1), (5, 0.8)],
#     [(0, 1), (1,0.5), (4, 2)]
# ]

# razdalje, poti = djikstra(razberiGraf('roadNet-TX.txt'), 0)

#razdalje, poti = djikstra(G, 0)

# G2 = [[(1,1), (2,3)],
#       [(4,4),(2,6),(3,1)],
#       [(4,3),(3,1),(6,6)],
#       [(6,2),(5,6)],[(6,2)],
#       [(7,3),(2,2)],[(7,1)],
#       []]
# 


# 
# razdalje, poti = djikstra(G2, 0)
# 
# print(razdalje)
# print(poti)
