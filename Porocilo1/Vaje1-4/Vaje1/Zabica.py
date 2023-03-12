#REKURZIVNO
from functools import lru_cache

def zabica(mocvara):
    @lru_cache(maxsize=None)
    def pobeg(k, e):
        if k >= len(mocvara):
            return 0
        else:
            e += mocvara[k]
            return 1 + min([pobeg(k + d, e - d) for d in range(1, e + 1)])
    return pobeg(0, 0)

#ITERATIVNO

def zabica_iter(mocvara):
    n = len(mocvara)
    # inicializacija seznama z vrednostmi 0
    max_dolzina = [0] * n

    # izračun največje dolžine za vsako količino energije
    for energija in range(1, n):
        for polje in range(n):
            for skok in range(1, energija+1):
                if polje + skok >= n:
                    # dosežemo končno polje, konec iskanja
                    return energija
                else:
                    # izračunamo dolžino, ki jo dosežemo s skokom
                    dolzina = max_dolzina[polje+skok] + mocvara[polje+skok]
                    if dolzina > max_dolzina[polje]:
                        max_dolzina[polje] = dolzina
    # če smo preiskali celotno močvaro in nismo našli poti, vrnemo -1
    return -1
