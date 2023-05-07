from djikstra import djikstra
from djikstra import djikstra_modificiran
from bfs import bfs
from bfs import bfs_modificiran


import time                         

import matplotlib.pyplot as plt     
import random


def preberi_graf(ime_datoteke):
    '''Iz datoteke prebere povezave grafa in jih zapiše v pravilno obliko (za G)'''
    with open(ime_datoteke, 'r') as f:
        vrstice = f.readlines()
    
    povezave = []
    for vrstica in vrstice[4:]:   #prve stiri vrstice so drugacne
        x, y = vrstica.strip().split()
        povezave.append((int(x), int(y)))

    # poiščemo koliko je vseh vozlišč (največje + 1)
    st_vozlisc = max(max(povezava) for povezava in povezave) + 1    ## najprej pogleda katero vozlišče v posameznem tuplu je večje, potem pogleda največjega od njih

    # naredimo seznam sosedov (G)
    seznam_sosedov = [[] for _ in range(st_vozlisc)]
    for u, v in povezave:
        seznam_sosedov[u].append((v, 1))  # vse povezave imajo ceno 1

    return seznam_sosedov



G = preberi_graf("roadNet-TX.txt")


x_djikstra = []
y_djikstra = []
for i in [100, 1000, 10000, 100000, 1000000]:
    porabljen_cas = 0
    for j in range(5):
        zacetek = time.time()
        djikstra(G, 100)
        konec = time.time()
        porabljen_cas += konec-zacetek
    povp_cas = porabljen_cas/5
    x_djikstra.append(i)
    y_djikstra.append(povp_cas)



x_djikstra_mod = []
y_djikstra_mod = []
for i in [100, 1000, 10000, 100000, 1000000]:
    porabljen_cas = 0
    for j in range(5):
        zacetek = time.time()
        djikstra_modificiran(G, 100, i)
        konec = time.time()
        porabljen_cas += konec-zacetek
    povp_cas = porabljen_cas/5
    x_djikstra_mod.append(i)
    y_djikstra_mod.append(povp_cas)
    
    
x_bfs = []
y_bfs = []
for i in [100, 1000, 10000, 100000, 1000000]:
    porabljen_cas = 0
    for j in range(5):
        zacetek = time.time()
        bfs(G, 100)
        konec = time.time()
        porabljen_cas += konec-zacetek
    povp_cas = porabljen_cas/5
    x_bfs.append(i)
    y_bfs.append(povp_cas)
    

x_bfs_mod = []
y_bfs_mod = []
for i in [100, 1000, 10000, 100000, 1000000]:
    porabljen_cas = 0
    for j in range(5):
        zacetek = time.time()
        bfs_modificiran(G, 100, i)
        konec = time.time()
        porabljen_cas += konec-zacetek
    povp_cas = porabljen_cas/5
    x_bfs_mod.append(i)
    y_bfs_mod.append(povp_cas)
    

plt.plot(x_djikstra, y_djikstra, label="djikstra")
plt.plot(x_djikstra_mod, y_djikstra_mod, label="djikstra modificirana")
plt.plot(x_bfs, y_bfs, label="BFS")
plt.plot(x_bfs_mod, y_bfs_mod, label="BFS modificiran")
plt.legend()
plt.title("Časovne zahtevnosti")
plt.savefig("cas_zahtevnost.png")
plt.show()
