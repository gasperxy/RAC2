from collections import deque
from naloga1 import seznam_sosednosti
from djikstra import djikstra
from graf import nov_graf
import time
import matplotlib.pyplot as plt

def BFS(G, s):
    """
    BFS vrne najkrajše poti od s do vseh ostalih vozlišč. Tu je s štartno 
    vozlišče, G pa je graf, ki je podan kot seznam sosednosti. Seznam d 
    predstavlja najkrajšo pot od vozlišča s do vseh ostalih.
    """
    n = len(G)

    # Nastavimo začetne vrednosti za sezname d, obiskani, in poti.
    d = [0] * n
    obiskani = [False] * n
    poti = [-1] * n
    q = deque([(s, 0, s)])

    while q:
        u, razdalja, p = q.popleft()

        if obiskani[u]: 
            continue

        obiskani[u] = True
        d[u] = razdalja
        poti[u] = p

        for sosed in G[u]:
            if not obiskani[sosed[0]]:
                q.append((sosed[0], razdalja + 1, u))
    return d, poti

def izmeri_case():
    """
    Izmeri case za Djikstro in BFS.
    """
    casi = []
    for v in range(1000, 100000, 1000):
        nov_graf(v)
        G = seznam_sosednosti()
        zacetniD = time.time()
        r1 = djikstra(G, 0)
        koncniD = time.time() - zacetniD
        zacetniBFS = time.time()
        r2 = BFS(G, 0)
        koncniBFS = time.time() - zacetniBFS
        casi.append((v, koncniD, koncniBFS))
        print(casi)
    return casi

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

def narisi():
    """
    Nariše graf za primerjanje Dijkstre in BFS.
    Grafi imajo pozitivne uteži.
    """
    casi = izmeri_case()
    sez_x = [cas[0] for cas in casi]
    sez_D = [cas[1] for cas in casi]
    sez_BFS = [cas[2] for cas in casi]
    plt.plot(sez_x, sez_D, "r")
    plt.plot(sez_x, sez_BFS, "b")
    plt.title("BFS (M) in Djikstra (R)")
    plt.xlabel("Število vozlišč")
    plt.ylabel("Potreben čas [s]")
    plt.savefig("BFS-D_primerjava.png")
    plt.show()


if __name__ == "__main__":
    narisi()
    # G = seznam_sosednosti()
    # razdalje, poti = BFS(G, 100)
    # print(razdalje[100000])
    # # Najbolj oddaljeno vozlišče
    # max_d = max(razdalje)
    # max_vozlisca = [i for i in range(len(razdalje)) if razdalje[i] == max_d]
    # print(max_vozlisca)
    # # Koliko vozlišč je dosegljivih iz 100
    # st_dosegljivi = len([d for d in razdalje if d > -1])
    # print(st_dosegljivi)

    
