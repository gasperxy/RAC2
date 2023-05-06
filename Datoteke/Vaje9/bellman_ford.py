from graf import nov_graf
# from naloga1 import seznam_sosednosti
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

        
def bellman_ford(G, s):
    """
    Vrne najkrajšo pot od začetnega vozlišča do vseh ostalih vozlišč.
    V primeru, da ima graf negativen cikel to izpiše.
    G je seznam sosednosti.
    """
    n = len(G)
    razdalje_do = [float("inf")] * n
    predhodnik = [None] * n
    razdalje_do[s] = 0
    for _ in range(n - 1):
        relax = False
        for u in range(n):
            for p in G[u]:
                v, w = p
                if razdalje_do[u] + w < razdalje_do[v]:
                    relax = True
                    razdalje_do[v] = razdalje_do[u] + w
                    predhodnik[v] = u
        if not relax:
            break

    # Preverimo ali obstaja negativen cikel
    for u in range(n):
        for p in G[u]:
            v, w = p
            if razdalje_do[u] != float("inf") and razdalje_do[u] + w < razdalje_do[v]:
                print("Graf ima negativen cikel!")
                return None
            
    return razdalje_do, predhodnik

def analiza_BF():
    """Analizira potreben čas za BF algoritem za različno število vozlišč."""
    casi = []
    for n in range(50000, 1000000, 50000):
        print(n)
        nov_graf(n)
        G = seznam_sosednosti()
        E = sum([len(e) for e in G])
        zacetni = time.perf_counter()
        razdalje = bellman_ford(G, 0)
        koncni = time.perf_counter() - zacetni
        casi.append((n, E, koncni))
    with open("casi.txt", "w") as f:
        for cas in casi:
            f.write(f"{cas[0]}\t{cas[1]}\t{cas[2]}\n")

if __name__ == "__main__":
    analiza_BF()
    # G = seznam_sosednosti()
    # 
    # razdalje, poti = bellman_ford(G, 100)
    # print(razdalje[100000])



