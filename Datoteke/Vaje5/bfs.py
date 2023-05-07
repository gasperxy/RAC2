from collections import deque  #za vrsto


def BFS(G, u):
    n = len(G)
    obiskani = [False] * n
    q = deque([u])   # zacnemo v u
    while q:
        trenutni = q.popleft()
        if obiskani[trenutni]:
            continue          # smo ga ze obiskali
        obiskani[trenutni] = True
        for sosed in G[trenutni]:
            if not obiskani[sosed]:
                q.push(sosed)      # dodamo soseda na desno stran vrste
                


def BFS_poti(G, u):
    '''Vrne najkrajše poti od u do vseh ostalih vozlišč.'''
    n = len(G)
    d = [0] * n
    obiskani = [False] * n
    q = deque([(u, 0)])
    while q:
        trenutni, razdalja = q.popleft()
        if obiskani[trenutni]:
            continue
        obiskani[trenutni] = True
        d[trenutni] = razdalja
        for sosed in G(trenutni):
            if not obiskani[sosed]:
                q.push((sosed, razdalja + 1))
    return d
    
    
def BFS_poti(G, u):
    '''Vrne najkrajše poti v neuteženem grafu G od u do vseh ostalih vozlišč.'''
    n = len(G)
    d = [0]*n  # vse razdalje na začetku nastavimo na 0
    obiskani = [False]*n
    q = deque([(u, 0)])  # drugi element=0 je razdalja i-tega vozlišča do u
    while q:
        trenutni, razdalja = q.popleft()
        if obiskani[trenutni]:
            continue
        else:
            obiskani[trenutni] = True
            d[trenutni] = razdalja
            for sosed in G[trenutni]:
                if not obiskani[sosed]:
                    # soseda dodamo na desno stran vrste
                    q.push((sosed, razdalja + 1))
    return d
