#Naloga1
from functools import lru_cache
def optimalni_tovor(predmeti, W):
    @lru_cache(maxsize=None)
    def poberi(i, P):
        if i == -1:
            if P >= 0:
                return 0
            else:
                return float('-inf')
        return max(poberi(i-1, P), poberi(i-1, P-predmeti[i][1])+predmeti[i][0])
    return poberi(len(predmeti)-1,W)

#Naloga2
def optimalni_predmeti(predmeti, W):
    predmeti = [(el[1],el[0]) for el in predmeti]
    n = len(predmeti)
    # matrika kjer hranimo vrednosti za vsak predmet in težo
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            # preverimo če trenutni predmet gre v nahrbtnik
            if predmeti[i-1][0] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-predmeti[i-1][0]] + predmeti[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]

    # preverimo katere predmete smo vzeli
    selected = list()
    j = W
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i-1][j]:
            selected.append(predmeti[i-1])
            j -= predmeti[i-1][0]
    
    selected = [(el[1],el[0]) for el in selected]
    return selected

#Naloga 3
from functools import lru_cache
def optimalni_tovor_zaloga(predmeti, W):
    nova = []
    for predmet in predmeti:
        if predmet[2] > 1:
            for _ in range(predmet[2]):
                nova.append(predmet)
        else:
            nova.append(predmet)
    @lru_cache(maxsize=None)
    def poberi(i, P):
        if i == -1:
            if P >= 0:
                return 0
            else:
                return float('-inf')
        return max(poberi(i-1, P), poberi(i-1, P-nova[i][1])+nova[i][0])
    return poberi(len(nova)-1,W)

#Naloga 4
def neomejena_zaloga(predmeti, W):
    @lru_cache(maxsize=None)
    def poberi(w):
        if w == 0:
            return 0 
        return max([poberi(w - v) + c for (c, v) in predmeti if v <= w] + [0])
    
    return poberi(W)