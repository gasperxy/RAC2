
from functools import lru_cache
import random
import time
from merilnik import *
def stevilo_poti(n, m, mine):
    mn_min = set(mine)
    @lru_cache(maxsize=None)
    def pomozna(i,j):
        if i >= n or j >= m:
            return 0
        elif i == n-1 and j == m-1:
            return 1
        elif (i,j) in mn_min:
            return 0
        else:
            desno = pomozna(i,j+1)
            dol = pomozna(i+1,j)
        return desno + dol
    return pomozna(0,0)





# generator testnih primerov

def generator_test_prim(n,m):
    '''Funkcija, ki zgenerira naključni testni primer, kjer sta vhodna podatka n in m, ki predstavljata širino
    oz. višino matrike.'''
    seznam_min = []
    for _ in range(round(n*m*random.random())):  # št. min naj bo naključno
        seznam_min.append((random.randint(0,n),random.randint(0,m)))
    return n,m,seznam_min


cas1 = time.time()
test1 = generator_test_prim(100,100)
cas2 = time.time()
cas_1 = cas2 - cas1


cas3 = time.time()
test2 = generator_test_prim(1000,1000)
cas4 = time.time()
cas_2 = cas4 - cas3


cas5 = time.time()
test3 = generator_test_prim(10000,1000)
cas6 = time.time()
cas_3 = cas6 - cas5



print(cas_1)
print(cas_2)
print(cas_3)





    