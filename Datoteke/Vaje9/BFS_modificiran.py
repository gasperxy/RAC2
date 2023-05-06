from collections import deque
def BFS_modificiran(G, s, t):
    """
    BFS vrne najkrajše poti od s do vseh ostalih vozlišč. Tu je s štartno 
    vozlišče, G je graf, ki je podan kot seznam sosednosti. t predstavlja
    končno vozlišče.
    """
    n = len(G)

    # Nastavimo začetne vrednosti za sezname d, obiskani, in poti.
    d = [0] * n
    obiskani = [False] * n
    poti = [-1] * n

    # Na vrsto dodamo trojico (v, d, p), kjer je: v vozlišče, d je razdalja, p 
    # pa prejšnje vozlišče na najkrajši poti od u do v.
    q = deque([(s, 0, s)])

    while q:
        u, razdalja, p = q.popleft()

        if obiskani[u]: 
            continue # smo ga že obiskali

        # obiščemo vozlišče ter nastavimo njegovo razdaljo
        # ter predhodnika na najkrajši poti od s do u
        obiskani[u] = True
        d[u] = razdalja
        poti[u] = p


        if u == t:
            break
        
        # gremo čez vse sosede in dodamo potrebne elemente na vrsto.
        for sosed in G[u]:
            if not obiskani[sosed[0]]:
                q.append((sosed[0], razdalja + 1, u)) #doda nov element v q
    return d, poti
