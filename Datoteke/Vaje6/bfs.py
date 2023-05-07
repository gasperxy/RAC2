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
                
                
