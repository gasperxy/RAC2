import time
from naloga2 import *

def ustvari_G(ime_datoteke):
    """
    Funkcija sprejme ime_datoteke in ustvari graf G kot seznam 
    sosednosti iz vozlišč, ki so zapisana na tej datekeki.
    """
    with open(ime_datoteke + ".txt", "r") as datoteka:
        vrstice = datoteka.readlines()
        n = vrstice[len(vrstice)-1].split("\t")[0]
        G = [[] for _ in range(int(n)+1)]
        for vrstica in vrstice:
            u, v, w = vrstica.split("\t")
            G[int(u)].append((int(v), int(w)))
    return G

def bellman_ford(G, s):
    """
    Funkcija sprejme graf G kot seznam sosednosti ter začetno vozlišče s.
    Vrne najkrajšo pot od začetnega vozlišča s do vseh ostalih vozlišč.
    V primeru, da ima graf negativen cikel to izpiše.
    """
    n = len(G)
    razdalje_do = [float("inf")] * n
    len(razdalje_do)
    predhodnik = [None] * n
    razdalje_do[s] = 0
    for _ in range(n - 1):
        sprememba = False
        for u in range(n):
            for p in G[u]:
                v, w = p
                if razdalje_do[u] + w < razdalje_do[v]:
                    sprememba = True
                    razdalje_do[v] = razdalje_do[u] + w
                    predhodnik[v] = u
        if not sprememba:
            break

    # Preverimo ali obstaja negativen cikel
    for u in range(n):
        for p in G[u]:
            v, w = p
            if razdalje_do[u] != float("inf") and razdalje_do[u] + w < razdalje_do[v]:
                print("Graf ima negativen cikel!")
                return None
    return razdalje_do

def casovna_analiza():
    """
    Funkcija analizira časovno zahtevnost Bellman Ford 
    algoritma za različno število vozlišč.
    """
    casi = []
    for n in range(1000, 80000, 1000):
        ustvari_graf(n)
        G = ustvari_G("ustvari_graf")
        st_povezav = sum([len(sosedi) for sosedi in G])
        zacetek = time.perf_counter()
        razdalje = bellman_ford(G, 0)
        konec = time.perf_counter() - zacetek
        casi.append((n, st_povezav, konec))
    with open("casovna_analiza.txt", "w") as datoteka:
        datoteka.write('Število vozlišč\tŠtevilo povezav\tBF\n')
        datoteka.write("-"*45 + "\n")
        for cas in casi:
            datoteka.write(f"{cas[0]}\t{cas[1]}\t{cas[2]}\n")

if __name__ == "__main__":
   #print(ustvari_G("Datoteke/Vaje9/ustvari_graf"))
   # print(ustvari_G)
   print(casovna_analiza())