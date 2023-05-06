import matplotlib.pyplot as plt
from djikstra import djikstra
from BFS import BFS
import time
from ustvari_graf import ustvari_graf
from BF import ustvari_G
from BFS_Djikstra_modificirana import *
#==============================================================================
# PRIMERJAVA BFS IN DJIKSTRE SPLOŠNO

def izmeri_case():
    """
    Izmeri čase za Dijkstro in BFS.
    """
    casi = []
    for n in range(1000, 50001, 500):
        ustvari_graf(n)
        G = ustvari_G("ustvari_graf")
        zacetekD = time.time()
        g1 = djikstra(G, 0)
        konecD = time.time() - zacetekD
        zacetekBFS = time.time()
        g2 = BFS(G, 0)
        konecBFS = time.time() - zacetekBFS
        casi.append((n, konecD, konecBFS))
    return casi

def narisi():
    """
    Nariše graf za primerjanje Dijkstre in BF.
    Grafi imajo pozitivne uteži.
    """
    casi = izmeri_case()
    sez_x = [cas[0] for cas in casi]
    sez_D = [cas[1] for cas in casi]
    sez_BFS = [cas[2] for cas in casi]
    plt.plot(sez_x, sez_D, "r", label="Djikstra")
    plt.plot(sez_x, sez_BFS, "b", label="BFS")
    plt.title("Primerjava časovne zahtevnost BFS in Dijkstra algoritmov")
    plt.xlabel("Število vozlišč")
    plt.ylabel("Potreben čas v [s]")
    plt.savefig("BFS-Djikstra-primerjava.png")
    plt.legend()
    plt.show()
#==============================================================================
# PRIMERJAVA BFS IN DJIKSTRE OD s do t VOZLIŠČA

def cas_pot(G, s, t):
    """
    Vrne potreben čas od začetnega vozlišča s do t za Djikstro in BFS.
    """
    d = []
    b = []
    for i in range(10):
        zacetni1 = time.time()
        r1 = djikstra_modificiran(G, s, t)
        koncni1 = time.time() - zacetni1
        d.append(koncni1)
    for _ in range(10):
        zacetni2 = time.time()
        r2 = BFS_modificiran(G, s, t)
        koncni2 = time.time() - zacetni2
        b.append(koncni2)
    return [sum(d) / 10, sum(b) / 10]

G = ustvari_G("ustvari_graf")
n = len(G)
def za_razlicne_k(n):
    casi = [[], [], []]
    for k in range(10, n, 2000):
        potreben_cas = cas_pot(G, 0, k)
        casi[0].append(k)
        casi[1].append(potreben_cas[0])
        casi[2].append(potreben_cas[1])
    return casi

def narisi_mod():
    """
    Nariše graf za primerjanje Dijkstre in BFS za neko končno vozlišče t, ki se spreminjajo.
    """
    casi = za_razlicne_k(len(G))
    sez_x = casi[0]
    sez_D = casi[1]
    sez_BFS = casi[2]
    plt.plot(sez_x, sez_D, "r", label="Djikstra")
    plt.plot(sez_x, sez_BFS, "b", label="BFS")
    plt.title("BFS in Djikstra pri različnih t in s = 0")
    plt.xlabel("k")
    plt.ylabel("Potreben čas [s]")
    plt.savefig("BFS_Djikstra_primerjava.png")
    plt.legend()
    plt.show()

if __name__=="__main__":
    narisi_mod()