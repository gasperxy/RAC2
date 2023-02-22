from functools import lru_cache

def stevilo_poti(n, m, mine):
    '''Vrne število pravih poti iz levega zgornjega kota do spodnjega desnega, glede na
        podana minska polja v matriki. Točke, kjer se nahajajo mine, so v vhodni tabeli.
        Matrika je velokosti n x m.
    '''
    # vse točke iz tabele mine damo v množico, zaradi nadaljnega hitrejšega iskanja točk
    # tako se le enkrat sprehodimo po tabeli
    mnozica_min = set(mine)
    
    @lru_cache(maxsize=None)
    def prestej_poti(i, j):
        # če pridemo do spodnjega desnega polja, smo zmagali
        if i == n-1 and j == m-1:
            return 1
        # če smo na minskem polju, to ni prava pot
        elif (i, j) in mnozica_min:
            return 0
        # če pademo izven matrike, nismo prišli do cilja
        elif i>=n or j>=m:
            return 0
        
        # pomaknemo se desno ali dol
        else:
            desno = prestej_poti(i, j+1)
            dol = prestej_poti(i+1, j)
            return desno + dol
    
    return prestej_poti(0, 0)


