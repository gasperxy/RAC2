from functools import lru_cache

def ali_ni_varno(matrika, i, j):
    return i<0 or i>=len(matrika) or j<0 or j>=len(matrika[0]) or matrika[i][j]==-1

def najvrednejsa_pot(matrika):
    n = len(matrika)
    m = len(matrika[0])
    
    @lru_cache(maxsize=None)
    def korak(i, j):
        '''i predstavlja vrstico, v kateri se nahajamo, j pa trenutni stolpec.'''
        if not matrika or not len(matrika):
            return 0
        
        elif ali_ni_varno(matrika, i, j):
            return 0        
        
        # če smo v sodi vrstici, gremo lahko desno ali pa dol
        if i%2 == 0:
            desno = korak(i, j+1)
            dol = korak(i+1, j)
            return matrika[i][j] + max(desno, dol)
        # če smo v lihi vrstice, gremo lahko levo ali dol
        else:
            levo = korak(i, j-1)
            dol = korak(i+1, j)
            return matrika[i][j] + max(levo, dol)
                
    return korak(0, 0)