from podatki import podatki, UstvariGraf
from collections import deque

def bfs_iskanje(G, u):
    '''Implemantacija BFS algoritma'''
    n = len(G)
    d = [0]*n
    obiskani = [False]*n
    q = deque([(u, 0)])
    while q:
        trenutni, razdalja = q.popleft()
        if obiskani[trenutni]:
            continue
        obiskani[trenutni] = True
        d[trenutni] = razdalja
        for sosed in G[trenutni]:
            if not obiskani[sosed[0]]:
                q.append((sosed[0], razdalja+1))
    return d

# Glavni program
if __name__ == "__main__" :
    n = podatki()[0]
    sez = podatki()[1]
    G = UstvariGraf(n, sez)
    print(G)
    razdalje = bfs_iskanje(G, 100)    

    #Koliko je razdalja dG(100,100000)?

    print(razdalje[100000])

    #Katero vozlišče je najbolj oddaljeno od vozlišča 100?

    # naj = max(razdalje)
    # indeks = razdalje.index(naj)
    # print(G[indeks])

    #Koliko vozlišč je dosegljivih iz vozlišča 100?

    #print(len(razdalje)) #1393383 
