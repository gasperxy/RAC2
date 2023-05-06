from podatki import podatki, UstvariGraf

def bfs_iskanje(G, u):
    '''Implemantacija BFS algoritma'''
    n = len(G)
    d = [-1]*n
    obiskani = [False]*n
    q = [(u,0,u)]
    poti = [None]*n
    while q:
        trenutni, razdalja, prej = q.pop(0)
        if obiskani[trenutni]:
            continue
        obiskani[trenutni] = True
        d[trenutni] = razdalja
        poti[trenutni] = prej
        for sosed, cena in G[trenutni]:
            if not obiskani[sosed]:
                q.append((sosed, razdalja+1, trenutni))
    return d, poti

# Glavni program
if __name__ == "__main__" :
    n = podatki()[0]
    sez = podatki()[1]
    G = UstvariGraf(n, sez)
    razdalje, poti = bfs_iskanje(G, 100)    

    #Koliko je razdalja dG(100,100000)?

    #print(razdalje[100000])

    #Katero vozlišče je najbolj oddaljeno od vozlišča 100?

    # naj = max(razdalje)
    # indeks = razdalje.index(naj)
    # print(G[indeks])

    #Koliko vozlišč je dosegljivih iz vozlišča 100?

    print(len(razdalje)) #1393383 
