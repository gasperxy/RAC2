import math
from functools import lru_cache

# 1. Podnaloga

def optimalni_tovor(predmeti, nosilnost):
    """Vrne najvecjo ceno za nosilnost 'W'."""
    slovar = dict()
    n = len(predmeti)
    def memo(ind, nosilnost):
        """Vrne najboljšo ceno."""
        if nosilnost < 0:
            return (-math.inf)
        if ind >= n:
            return 0
        if (ind, nosilnost) in slovar:
            return slovar[(ind, nosilnost)]
        vzamemo_tovor = memo(ind + 1, nosilnost - predmeti[ind][1]) + predmeti[ind][0]
        ne_vzamemo_tovor = memo(ind + 1, nosilnost)
        boljsi = max(ne_vzamemo_tovor, vzamemo_tovor)
        slovar[(ind, nosilnost)] = boljsi
        return slovar[(ind, nosilnost)]
    return memo(0, nosilnost)

# 3. Podnaloga

def optimalni_tovor_zaloga(predmeti, nosilnost):
    '''Vrne najvecjo skupno ceno, ki jo lahko trgovec natovori'''
    # opt_cena = optimalni_tovor(predmeti, nosilnost)
    return optimalni_tovor(pomnozi(predmeti), nosilnost)
    
def pomnozi(tab):
    nova_tab = []
    for oklepaj in tab:
        for _ in range(oklepaj[2]):
            nova_tab.append(oklepaj[:2])
    return nova_tab

# 4. Podnaloga

def cena_na_volumen(element):
    """Izračuna ceno na volumen."""
    return element[0] / element[1]

def neomejena_zaloga(predmeti, W):
    urejeni = sorted(predmeti, key=cena_na_volumen, reverse=True)
    cena = 0
    for element in urejeni:
        while W - element[1] > 0:
            cena += element[0]
            W -= element[1]
    return cena 

# 6. Podnaloga

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

if __name__ == "__main__":
    tovor1 = [(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)]
    tovor2 = [(90, 4942), (28, 3173), (58, 3515), (76, 637), (9, 5404), (29, 8912), (25, 753), (7, 186), (10, 6055),\
              (58, 7686), (89, 7892), (5, 6709), (43, 7281), (85, 6171), (34, 7676), (54, 5481), (65, 6972), (7, 5146),\
              (48, 5487), (71, 7110), (21, 8080), (25, 3948), (25, 8008), (4, 2765), (58, 7509), (85, 2432), (57, 3933),\
              (23, 639), (18, 7577), (41, 7038), (62, 7685), (23, 4659), (48, 5920), (21, 1924), (63, 6688), (19, 6309),\
              (73, 6807), (30, 2201), (22, 9218), (77, 6274), (68, 4114), (27, 7668), (54, 3871), (49, 5739), (55, 1298),\
              (89, 7515), (20, 3797), (6, 732), (16, 2778), (69, 3293)]
    tovor1_zaloge = [(2,3, 1), (4,4, 2), (5,4, 4), (3,2, 3), (1,2, 3), (15, 12, 2)]
    print(optimalni_tovor(tovor1, 7) == 8)
    print(optimalni_tovor(tovor2, 100000) == 1425)
    print(optimalni_tovor_zaloga(tovor1_zaloge, 7) == 9)
    print(neomejena_zaloga(tovor1, 23) == 33)
    print(tovor_rezanje(tovor1, 20) == 25.0)    