import matplotlib.pyplot as plt
from djikstra import djikstra
from bellman_ford import bellman_ford
import time
from graf import nov_graf
from bellman_ford import seznam_sosednosti

def izmeri_case():
    """
    Izmeri case za Dijkstro in BF.
    """
    casi = []
    for v in range(1000, 50000, 1000):
        nov_graf(v)
        G = seznam_sosednosti()
        zacetniD = time.time()
        r1 = djikstra(G, 0)
        koncniD = time.time() - zacetniD
        zacetniBF = time.time()
        r2 = bellman_ford(G, 0)
        koncniBF = time.time() - zacetniBF
        casi.append((v, koncniD, koncniBF))
        print(casi)
    return casi



def narisi():
    """
    Nariše graf za primerjanje Dijkstre in BF.
    Grafi imajo pozitivne uteži.
    """
    casi = izmeri_case()
    sez_x = [cas[0] for cas in casi]
    sez_D = [cas[1] for cas in casi]
    sez_BF = [cas[2] for cas in casi]
    plt.plot(sez_x, sez_D, "r")
    plt.plot(sez_x, sez_BF, "b")
    plt.title("Bellman-Ford in Dijkstra")
    plt.xlabel("Število vozlišč")
    plt.ylabel("Potreben čas [s]")
    plt.savefig("BF-D_primerjava.png")
    plt.show()


if __name__ == "__main__":
    narisi()