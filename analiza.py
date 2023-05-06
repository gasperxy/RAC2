# import matplotlib.pyplot as plt
# import time
# from dijsktra import *
# from BFS import *
# from dijsktra_2 import *
# from BFS_2 import *
# 
# 
# def naj():
#     naj = 0
#     with open('roadNet-TX.txt', 'r') as f:
#         vrstice = f.readlines()
#         veljavne = vrstice[4:]
#         for vrstica in veljavne:
#             trenutna = vrstica.strip().split("\t")
#             od = int(trenutna[0])
#             do = int(trenutna[1])
#             if od > naj:
#                 naj = od
#     return naj
# 
# 
# def omrezje(n):
#     vse = [[] for _ in range(n+1)]
#     with open('roadNet-TX.txt', 'r') as f:
#         vrstice = f.readlines()
#         veljavne = vrstice[4:]
#         for vrstica in veljavne:
#             trenutna = vrstica.strip().split("\t")
#             od = int(trenutna[0])
#             do = int(trenutna[1])
#             vse[od].append((do, 1))
#     return vse
# 
# 
# rez = omrezje(naj())
# 
# 
# x4 = []
# y4 = []
# 
# for i in [100, 1000, 10000, 100000, 1000000]:
#     skupaj = 0
#     for _ in range(6):
#         zacetek = time.time()
#         BFS_2(rez, 100, i)
#         konec = time.time()
#         skupaj += konec-zacetek
#     x4.append(i)
#     y4.append(skupaj/6)
# 
# 
# x3 = []
# y3 = []
# 
# for i in [100, 1000, 100000, 1000000]:
#     skupaj = 0
#     for _ in range(6):
#         zacetek = time.time()
#         BFS(rez, 100)
#         konec = time.time()
#         skupaj += konec-zacetek
#     x3.append(i)
#     y3.append(skupaj/6)
# 
# 
# x2 = []
# y2 = []
# 
# for i in [100, 1000, 10000, 100000, 1000000]:
#     skupaj = 0
#     for _ in range(6):
#         zacetek = time.time()
#         dijkstra_2(rez, 100, i)
#         konec = time.time()
#         skupaj += konec-zacetek
#     x2.append(i)
#     y2.append(skupaj/6)
# 
# x1 = []
# y1 = []
# 
# for i in [100, 1000, 100000, 1000000]:
#     skupaj = 0
#     for _ in range(6):
#         zacetek = time.time()
#         dijkstra(rez, 100)
#         konec = time.time()
#         skupaj += konec-zacetek
#     x1.append(i)
#     y1.append(skupaj/6)
# 
# plt.plot(x1, y1, label="djikstra samo začetek")
# plt.plot(x2, y2, label="djikstra začetek in konec")
# plt.plot(x3, y3, label="bfs samo začetek")
# plt.plot(x4, y4, label="bfs začetek in konec")
# plt.title("Časovna zahtevnost")
# plt.legend()
# # plt.savefig("cas_zahtevnost.pdf")
# plt.show()

import time                         # Štoparica

import matplotlib.pyplot as plt     # Risanje grafov
import random                       # Za generiranje primerov

from dijsktra import *
from BFS import *

def pretvori_v_seznam(datoteka):
    '''Funkcija prebere datoteko in v seznam shrani vse povezave'''
    seznam = []
    with open(datoteka, 'r') as file:
        for vrstica in file:
            if vrstica[0] == '#': continue
            else:
                podatki = vrstica.split('\t')
                seznam.append((int(podatki[0]), int(podatki[1])))
    seznam.sort(key=lambda x: x[0], reverse=True)
                
    return seznam

#seznam povezav
povezave = pretvori_v_seznam('roadNet-TX.txt')

def ustvari_graf(povezave):
    '''Funkcija naredi seznam sosednosti'''
    G = [list() for _ in range(povezave[0][0]+1)]
    for i in povezave:
        u,v = i[0],i[1]
        G[u].append((v, 1)) #uteži so enake 1
    return G

#ustvarimo graf
graf = ustvari_graf(povezave)

def djikstra_dodelan(G, s, t):
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

        if u == t: #V primeru da je u naše željeno končno vozlišče zaključimo s to zanko in končamo
            break

        # gremo čez vse sosede in dodamo potrebne elemente na vrsto.
        for (v, teza) in G[u]:
            if not obiskani[v]:

                # heap.heappush(Q, elem) doda element v seznam Q, kjer ohranja lastnost kopice.
                heapq.heappush(Q, (razdalja + teza, v, u))

    return razdaljeDo, poti

def BFS_dodelan(G, u, t):
    '''Funkcija vrne seznam poti od vozlisca u do vozlišča t v grafu G'''
    n = len(G)
    razdalje = [0]*n
    obiskani = [False]*n
    q = ([(u,0,u)]) #začnemo v u, razdlaja je na začetku 0
    poti =[None]*n
    while q: #dokler vrsta ni prazna
        trenutni, razdalja, prejsni = q.pop(0)
        if obiskani[trenutni]:
            continue #soseda smo že obiskali

        if trenutni == t:
            break 
        #v primeru da smo prišli do našega željenga končnega vozlišča t zaključimo s to zanko
        obiskani[trenutni] = True
        razdalje[trenutni] = razdalja
        poti[trenutni] = prejsni
        for sosed, teza in G[trenutni]:
            if not obiskani[sosed]:
                q.append((sosed, razdalja +1, trenutni)) #v vrsto dodamo soseda,razdalji prištejemo ena
    return razdalje, poti


vozlisce = [1,10,100,1000,10000,100000,1000000]
#Dijkstra-nedodelana

casi_d1 = []
cas_d1 = 0

for i in vozlisce:
    zacetek = time.perf_counter()
    dijkstra(graf,i)
    konec = time.perf_counter()
    cas_d1 += konec - zacetek
    casi_d1.append(cas_d1)

#dijkstra dodelana

casi_d2 = []
cas_d2 = 0

for i in vozlisce:
    zacetek = time.perf_counter()
    djikstra_dodelan(graf,1,i)
    konec = time.perf_counter()
    cas_d2 += konec - zacetek
    casi_d2.append(cas_d2)
    
#BFS

casi_b1 = []
cas_b1 = 0

for i in vozlisce:
    zacetek = time.perf_counter()
    BFS(graf,i)
    konec = time.perf_counter()
    cas_b1 += konec - zacetek
    casi_b1.append(cas_b1)
    
#BFS dodelan
    
casi_b2 = []
cas_b2 = 0

for i in vozlisce:
    zacetek = time.perf_counter()
    BFS_dodelan(graf,1,i)
    konec = time.perf_counter()
    cas_b2 += konec - zacetek
    casi_b2.append(cas_b2)
    
    
print(casi_d1)
print(casi_d2)
print(casi_b1)
print(casi_b2)

x_os = [1,2,3,4,5,6,7]

plt.grid(linestyle = '-', linewidth = 0.5)
plt.xlabel('Število vozlišč')
plt.ylabel('Potreben čas [s]')
plt.plot(x_os, casi_d1, label='Dijkstra - nedodelan')
plt.plot(x_os, casi_d2, label='Dijkstra - dodelan')
plt.plot(x_os, casi_b1, label='BFS - nedodelan')
plt.plot(x_os, casi_b2, label='BFS - dodelan')
plt.legend()
plt.show()