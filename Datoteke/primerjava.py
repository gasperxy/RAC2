import time                         

import matplotlib.pyplot as plt     
import random
import heapq  # kopica
from collections import deque
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






def BFS(G, s):
    '''vrne najkrajše poti od u do vseh vozlisc'''
    n = len(G)
    razdalje = [0]*n
    obiskani = [False]*n
    q = [(s, 0, s)]  # začnemo v u
    poti = [None]*n
    while q:
        trenutni, razdalja, pred = q.pop(0)
        if obiskani[trenutni]:
            continue
        obiskani[trenutni] = True
        razdalje[trenutni] = razdalja
        poti[trenutni] = pred
        for sosed, cena in G[trenutni]:
            if not obiskani[sosed]:
                q.append((sosed, razdalja+1, trenutni))
    return razdalje, poti




# def BFS_druga(G, u, t):
#         '''Funkcija, ki vrne razdaljo med s in t v grafu G ter pot (kot drevo) med njima.'''
#     n = len(G)
#     d = [0]*n
#     obiskani = [False]*n
#     q = [(u, 0, u)]  # začnemo v u
#     poti = [None] * n
#     while q:
#         trenutni, razdalja, prej = q.pop(0)
#         if obiskani[trenutni]:
#             continue
#         obiskani[trenutni] = True
#         d[trenutni] = razdalja
#         poti[trenutni] = prej
# 
#         if trenutni == t:
#             break
# 
#         for sosed, cena in G[trenutni]:
#             if not obiskani[sosed]:
#                 q.append((sosed, razdalja+1, trenutni))
#     return d, poti
# 




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








# primerjava časovne zahtevnosti
primer1 = datoteka("roadNet-TX.txt")
graf = seznam_sosednosti(primer1)


x_os1 = []
y_os1 = []

for i in [100, 1000, 100000, 1000000]:
    skupaj = 0
    for _ in range(5):
        zacetek = time.time()
        djikstra(graf, 100)
        konec = time.time()
        skupaj += konec-zacetek
    x_os1.append(i)
    y_os1.append(skupaj/5)


x_os2 = []
y_os2 = []

for i in [100, 1000, 100000, 1000000]:
    skupaj = 0
    for _ in range(5):
        zacetek = time.time()
        djikstra_druga(graf, 100,i)
        konec = time.time()
        skupaj += konec-zacetek
    x_os2.append(i)
    y_os2.append(skupaj/5)
    
    
x_os3 = []
y_os3 = []

# for i in [10, 100, 1000, 100000, 1000000]:
#     skupaj = 0
#     for _ in range(5):
#         zacetek = time.time()
#         BFS_druga(graf, 100,i)
#         konec = time.time()
#         skupaj += konec-zacetek
#     x_os3.append(i)
#     y_os3.append(skupaj/5)
#     

x_os4 = []
y_os4 = []

for i in [100, 1000, 100000, 1000000]:
    skupaj = 0
    for _ in range(5):
        zacetek = time.time()
        BFS(graf, 100)
        konec = time.time()
        skupaj += konec-zacetek
    x_os4.append(i)
    y_os4.append(skupaj/5)

plt.plot(x_os1, y_os1, label="djikstra")
plt.plot(x_os2, y_os2, label="djikstra izboljšana")
plt.plot(x_os4, y_os4, label="BFS")
plt.title("Časovna zahtevnost")
plt.legend()
# plt.savefig("cas_zahtevnost.pdf")
plt.show()













