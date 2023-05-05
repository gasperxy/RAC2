def bfs(G,u):
    n = len(G)
    obiskani = [False]*n
    q = vrsta([u]) #začnemo v u
    while q:
        trenutni = q.popleft()
        if obiskani[trenutni]: continue
        obiskani[trenutni] = True
        from sosed in G[trenutni]:
            if not obiskani[sosed]:
                q.push(sosed)
    
    
    
def bfs_iskanje(G,u):
    '''vrne najkrajše poti od u do vseh vozlisc'''
    n = len(G)
    d = [0]*n
    obiskani = [False]*n
    q = vrsta([(u,0)]) #začnemo v u
    while q:
        trenutni,razdalja = q.popleft()
        if obiskani[trenutni]: continue
        obiskani[trenutni] = True
        d[trenutni] = razdalja
        from sosed in G[trenutni]:
            if not obiskani[sosed]:
                q.push((sosed,razdalja+1))
    return d