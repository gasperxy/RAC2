from minsko_polje_iterativno import stevilo_poti_iterativno
from minsko_polje import stevilo_poti
import matplotlib.pyplot as plt
import random
import time


def gen_mine(n, m, st_tock):
    '''Generira množico točk (x, y), kjer gre x-koordinata od 0 do n in y od 0 do m.
        Število takih točk nam pove parameter `st_tock`.
    '''
    mnozica = set((random.randint(0, n), random.randint(0, m)) for _ in range(st_tock))
    if (0, 0) in mnozica:
        # na začetnem polju ni mine
        mnozica.remove((0, 0))
        mnozica.add((random.randint(1, n-1), random.randint(1, m-1)))
    if (n-1, m-1) in mnozica:
        # na končnem polju ni mine
        mnozica.remove((n-1, m-1))
        mnozica.add((random.randint(1, n-1), random.randint(1, m-1)))
    return mnozica


def izmeri_cas_mine(fun, n, m, primer):
    '''Izmeri čas izvajanja funkcije `fun` pri argumentu `primer`.
    '''
    cas1 = time.perf_counter()
    fun(n, m, primer)
    cas2 = time.perf_counter()
    cas = cas2 - cas1
    return cas


# Na matriki velikosti 17x18 kličemo funkcijo Minsko polje za število min od 10 do 150, po 10
testi = list()
for i in range(10, 151, 10):
    testi.append(gen_mine(17, 18, i))

tab_rekurzivno = list()
tab_iterativno = list()
for mn in testi:
    tab_rekurzivno.append(izmeri_cas_mine(stevilo_poti, 17, 18, mn))
    tab_iterativno.append(izmeri_cas_mine(stevilo_poti_iterativno, 17, 18, mn))

def izpisi_case(tab):
    n = len(tab)
    # za lepšo poravnavo izračunamo širino levega stolpca
    pad = n
    dol = max([len(str(x)) for x in tab])
    sep_len = pad + dol + 3

    # izpiši glavo tabele
    print("{:{pad}} | Čas izvedbe [s]".format("Število min", pad=pad))
    # horizontalni separator
    sep_len = pad + dol + 3 
    print("-"*sep_len)
    
    st = 10
    # izpiši vrstice
    for i in range(n):
        print('{:{}} | {}'.format(st, pad, tab[i]))
        st += 10

    # končna tabela naj izgleda približno takole (seveda pa jo lahko polepšate):
    # n  | Čas izvedbe [s]
    # ---------------------------
    # 10 | 4.198900114715798e-06 
    # 20 | 1.6393299847550225e-05
    # 30 | 3.7693600006605266e-05

def narisi_in_pokazi_graf(tocke):
    x_os = [_ for _ in range(len(tocke))]
    plt.plot(x_os, tocke, 'r')
    plt.savefig('graf.png')
    plt.show()


# Izpis časov izvajanja funkcije `Minsko polje` REKURZIVNO
print('Minsko polje - rekurzivno')
izpisi_case(tab_rekurzivno)


# Izpis časov izvajanja funkcije `Minsko polje` ITERATIVNO
print('\n')
print('Minsko polje - iterativno')
izpisi_case(tab_iterativno)


razlike = list()
for i in range(15):
    razlike.append(abs(tab_rekurzivno[i] - tab_iterativno[i]))

narisi_in_pokazi_graf(razlike)



