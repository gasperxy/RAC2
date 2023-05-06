from djikstra import djikstra
from BellmanFord import BellmanFord, podatki

import time                         # Štoparica
import matplotlib.pyplot as plt     # Risanje grafov
import random                       # Za generiranje primerov


def oceni_potreben_cas_djikstra(fun, gen_graf, n, k):
    """ Funkcija oceni potreben čas za izvedbo funkcije `fun` na primerih
    dolžine `n`. Za oceno generira primere primerne dolžine s klicom
    `gen_primerov(n)`, in vzame povprečje časa za `k` primerov. """

    zac = time.perf_counter()
    for _ in range(k):
        fun(gen_graf(n)[1], 0)
    konc = time.perf_counter()
    return (konc - zac) / k

def oceni_potreben_cas_BF(fun, gen_graf, n, k):
    """ Funkcija oceni potreben čas za izvedbo funkcije `fun` na primerih
    dolžine `n`. Za oceno generira primere primerne dolžine s klicom
    `gen_primerov(n)`, in vzame povprečje časa za `k` primerov. """

    zac = time.perf_counter()
    for _ in range(k):
        fun(test(gen_graf(n)[1]), 0, len(gen_graf(n)[1]))
    konc = time.perf_counter()
    return (konc - zac) / k

def primerjaj_case_dveh(fun1, fun2, gen_graf, sez_n, k=5):
    """ Funkcija izpiše tabelo časa za izračun 'fun1' in 'fun2' na primerih generiranih z
    `gen_primerov`, glede na velikosti primerov v `sez_n`. Za oceno uporabi `k`
    ponovitev. Funkcija tudi nariše graf kjer še lažje opazimo razliko med delovanjem funkcijama. """

    # Seznam časov, ki jih želimo tabelirati
    casi1, casi2 = [], []
    for el in sez_n:
        casi1.append(oceni_potreben_cas_djikstra(fun1, gen_graf, el, k))
        casi2.append(oceni_potreben_cas_BF(fun2, gen_graf, el, k))
        
    # za lepšo poravnavo izračunamo širino levega stolpca
    maks = max(sez_n)
    pad = len(str(maks)) + 1
    # izpiši glavo tabele
    
    print("{:{pad}} | Čas izvedbe[s](fun1)   | Čas izvedbe[s](fun2)".format("n", pad=pad))
    
    # horizontalni separator
    sep_len = len(str(max(casi1))) + len(str(max(casi2))) + pad + 8  # DOPOLNITE KODO (črta naj bo široka kot najširša vrstica)
    print("-"*sep_len)

    # izpiši vrstice
    for i in range(len(sez_n)):
        razmik1 = ' '*(pad - len(str(sez_n[i]))+1)
        print(str(sez_n[i]) + razmik1 + '| ' + str(casi1[i]) + razmik1 + '| ' + str(casi2[i]))
        
    #Izris grafa.
    plt.grid(linestyle = '-', linewidth = 0.5)
    plt.plot(sez_n, casi1, label = 'Djikstra')        
    plt.plot(sez_n, casi2, label = 'Bellman-Ford') 
    plt.xlabel('Velikost problema.')
    plt.ylabel('Potreben cas [s]')
    plt.title('Primerjava časovne zahtevnosti dveh funkcij.')
    plt.legend()
    plt.show()
    
def gen_graf(n):
     '''Generiramo testne grafe, predstavljene kot sezname sosednosti
        Dobljeno od Diane Skof'''
     graf1 = [[] for _ in range(n)] # vozlišča od 0 do st_vozlisc-1
     graf2 = [[] for _ in range(n)]  # vozlišča od 0 do st_vozlisc-1
     for i in range(n):
         mn = set()  # da se sosedje ne ponavljajo
         for j in range(random.randint(0, n-1)):  # random koliko sosedov bo imelo i-to vozlišče
             stevilo = random.randint(0, n-1)
             mn.add(stevilo)
         for elt in mn:
             graf1[i].append(elt)
             graf2[i].append((elt, 1))
     return graf1, graf2


def test(graf):
    sez = []
    for i, sosedje in enumerate(graf):
        for sosed in sosedje:
            sez.append((i, int(sosed[0]), int(sosed[1])))
    return sez

if __name__ == '__main__':
    print(primerjaj_case_dveh(djikstra, BellmanFord, gen_graf, [100,200,300,400,500,600,700,800,900,1000], k=5))