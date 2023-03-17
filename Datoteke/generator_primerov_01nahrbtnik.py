import time                         # Štoparica
import random                       # Za generiranje primerov


def izmeri_cas(fun, predmeti, volumen_nahrbtnika):
    """Izmeri čas izvajanja funkcije `fun` pri argumentu `predmeti` in `volumen_nahrbtnika`."""
    zacetek = time.time()
    x = fun(predmeti, volumen_nahrbtnika)
    konec = time.time()
    return konec - zacetek

def oceni_potreben_cas(fun, test_gen_sez, max_cena, max_volumen, n, volumen_nahrbtnika, k):
    """ Funkcija oceni potreben čas za izvedbo funkcije `fun` na primerih
    dolžine `n`. Za oceno generira primere primerne dolžine s klicom
    `test_gen_sez`, in vzame povprečje časa za `k` primerov. """
    vsota = 0
    for i in range(k):
        vsota += izmeri_cas(fun, test_gen_sez(max_cena, max_volumen, n), volumen_nahrbtnika)
    povprecje = vsota/k
    return povprecje

# -----------------------------------------------------------------------------

import math
from functools import lru_cache
def optimalni_tovor(predmeti, W):
    n = len(predmeti)
    
    @lru_cache(maxsize=None)
    def b(i,R):
        if i == -1 and R < 0:
            return float('-inf')
        if i == -1 and R >=0:
            return 0
        return max(predmeti[i][0] + b(i-1,R-predmeti[i][1]), b(i-1,R))
    return b(n-1,W)

def test_gen_sez(max_cena, max_volumen, n):
    """Generira testni seznam dolžine n. Pri čemer je cena od 1 do max_cene
    (saj se predmetov z ceno 0 ne bi 'splačalo' vzeti sabo) in volumen od 1 do max_volumen."""
    
    return [(random.randint(1, max_cena), random.randint(1, max_cena)) for _ in range(n)]

# -----------------------------------------------------------------------------

if __name__ == '__main__':
#    print(oceni_potreben_cas(optimalni_tovor, test_gen_sez, 50, 30, 50, 30, 12))
    print(oceni_potreben_cas(optimalni_tovor, test_gen_sez, 50, 30, 30, 30, 12))
    print(oceni_potreben_cas(optimalni_tovor, test_gen_sez, 50, 30, 100, 30, 12))
    print(oceni_potreben_cas(optimalni_tovor, test_gen_sez, 50, 30, 150, 30, 12))

