

import matplotlib.pyplot as plt
from functools import wraps
import time


def timeit(func):
    """
    Dekorator, ki vrne čas izvajanja funkcije.
    """
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
       
        return total_time
    return timeit_wrapper

@timeit
def zmnozi(a,b):
    return a*b



# testni podatki za našo funkcijo
testi = [
    (12*10**3, 13*10**3),
    (12*10**6, 13*10**6),
    (12*10**12, 13*10**12),
    (12*10**24, 13*10**24),
    (12*10**48, 13*10**48),
    (12*10**96, 13*10**96),
    (12*10**192, 13*10**192),
    (12*10**400, 13*10**400),
    (12*10**800, 13*10**800),
    (12*10**1600, 13*10**1600)
    ]

# Pripravimo x in y koordinate za graf
x = [a.bit_length() +b.bit_length() for a,b in testi]
y =[zmnozi(a,b) for a,b in testi]

# Zgradimo preprost graf
plt.scatter(x, y, c ="blue")
plt.xlabel("Število bitov")
plt.ylabel("Čas [s]")
 
# Shranimo sliko 
plt.savefig('Datoteke/Vaje1/zmnozi_cas.png')


plt.show()
