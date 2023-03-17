from functools import lru_cache
# 1. NALOGA
def optimalni_tovor(predmeti, W):
    """Vrne največjo skupno ceno predmetov."""
    @lru_cache(maxsize = None)
    def poberi(i, p):
        if i == -1:
            if p >= 0:
                return 0
            else:
                return -float('inf')
        return max(poberi(i - 1, p), poberi(i - 1, p - predmeti[i][1]) + predmeti[i][0])
    return poberi(len(predmeti) - 1, W)

# 3. NALOGA
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
                return float("-inf")
        return max(poberi(i - 1, P), poberi(i - 1, P - nova[i][1]) + nova[i][0])
    return poberi(len(nova) - 1, W)

# 4. NALOGA
def cena_na_volumen(element):
    """Izračuna ceno na volumen."""
    return element[0] / element[1]

def neomejena_zaloga(predmeti, W):
    urejeni = sorted(predmeti, key=cena_na_volumen, reverse=True)
    cena = 0
    for element in urejeni:
        n = W // element[1]
        cena += element[0] * n
        W -= n * element[1]
    return cena

# 6. NALOGA
from functools import lru_cache
def tovor_rezanje(predmeti, W):
    """Vrne največjo skupno ceno za nosilnost 'W', pri čemer predemete lahko režemo."""
    @lru_cache(maxsize=None)
    def max_cena(i, w):
        if w < 0:
            return float("-inf")
        if i == 0 or w == 0:
            return 0
        c = predmeti[i-1][0]
        v = predmeti[i-1][1]
        return max(c + max_cena(i-1, w-v), max_cena(i-1, w), c/2 + max_cena(i-1, w-v/2), c/3 + max_cena(i-1, w-v/3), c/4 + max_cena(i-1, w-v/4))

    return round(max_cena(len(predmeti), W),2)