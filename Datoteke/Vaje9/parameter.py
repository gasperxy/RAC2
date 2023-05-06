import matplotlib.pyplot as plt
from dijkstra_modificiran import djikstra_modificiran
from BFS_modificiran import BFS_modificiran
import time

def seznam_sosednosti():
    """
    Sestavi seznam sosednosti iz grafa zapisanega v tekstovni datoteki.
    """
    with open("nov_graf.txt", "r") as f:
        vrstice = f.readlines()
    n = len({vrstica.split("\t")[0] for vrstica in vrstice})
    print(n)
    G = [[] for _ in range(n)]
    for vrstica in vrstice:
        u, v, w = vrstica.split("\t")
        G[int(u)].append((int(v), int(w)))
    return G


def cas_pot(G, s, k):
    """
    Vrne potreben čas od začetnega vozlišča 0 do k za Djikstro in BFS.
    """
    d = []
    b = []
    for i in range(15):
        zacetni1 = time.time()
        r1 = djikstra_modificiran(G, s, k)
        koncni1 = time.time() - zacetni1
        d.append(koncni1)
    for _ in range(15):
        zacetni2 = time.time()
        r2 = BFS_modificiran(G, s, k)
        koncni2 = time.time() - zacetni2
        b.append(koncni2)
    return [sum(d) / 15, sum(b) / 15]



G = seznam_sosednosti()
n = len(G)
def za_razlicne_k(n):
    casi = [[], [], []]
    for k in range(10, n, 3000):
        print(k)
        potreben_cas = cas_pot(G, 0, k)
        casi[0].append(k)
        casi[1].append(potreben_cas[0])
        casi[2].append(potreben_cas[1])
    return casi

def narisi():
    """
    Nariše graf za primerjanje Dijkstre in BFS za neko končno vozlišče t, ki se spreminjajo.
    """
    casi = za_razlicne_k(len(G))
    sez_x = casi[0]
    sez_D = casi[1]
    sez_BFS = casi[2]
    plt.plot(sez_x, sez_D, "r")
    plt.plot(sez_x, sez_BFS, "b")
    plt.title("BFS (M) in Djikstra (R) pri različnih t in s = 0")
    plt.xlabel("k")
    plt.ylabel("Potreben čas [s]")
    plt.savefig("BFS-D-K_primerjava.png")
    plt.show()

if __name__ == "__main__":
    narisi()