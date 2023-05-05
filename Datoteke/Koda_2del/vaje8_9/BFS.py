import queue


def bfs(G, u):
    n = len(G)
    obiskani = [False]*n
    q = vrsta([u])  # začnemo v u
    while q:
        trenutni = q.popleft()
        if obiskani[trenutni]:
            continue
        obiskani[trenutni] = True
        for sosed in G[trenutni]:
            if not obiskani[sosed]:
                q.push(sosed)


def bfs_iskanje(G, u):
    '''vrne najkrajše poti od u do vseh vozlisc'''
    n = len(G)
    d = [0]*n
    obiskani = [False]*n
    q = queue.Queue()
    q.put((u, 0))  # začnemo v u
    while q:
        print(q.get())
        trenutni, razdalja = q.get()
        if obiskani[trenutni]:
            continue
        obiskani[trenutni] = True
        d[trenutni] = razdalja
        for sosed in G[trenutni]:
            if not obiskani[sosed]:
                q.put((sosed, razdalja+1))
    return d


def bfs_iskanje2(G, u):
    '''vrne najkrajše poti od u do vseh vozlisc'''
    n = len(G)
    #d = [float("inf")]*n
    d = [0]*n
    obiskani = [False]*n
    q = [(u, 0, u)]  # začnemo v u
    poti = [None]*n
    while q:
        trenutni, razdalja, pred = q.pop(0)
        if obiskani[trenutni]:
            continue
        obiskani[trenutni] = True
        d[trenutni] = razdalja
        poti[trenutni] = pred
        for sosed, cena in G[trenutni]:
            if not obiskani[sosed]:
                q.append((sosed, razdalja+1, trenutni))
    return d, poti
