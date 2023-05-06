from collections import Deque

def BFS(G, u):
    """ 
    Funkcija sprejme graf G predstavljen kot seznam sosedov 
    in startno vozlisce u ter naredi pregled v širino.
    """
    n = len(G)
    obiskani = [False] * n
    # Začnemo v u. V primeru DFS-ja to spremenimo v sklad.
    q = vrsta([u]) 

    while q:
        trenutni = q.popleft()
        # Soseda smo že obiskali
        if obiskani[trenutni] : 
            continue 
        obiskani[trenutni] = True
        for sosed in G[trenutni]:
            if not obiskani[sosed]:
                # Doda nov element v q
                q.push(sosed) 