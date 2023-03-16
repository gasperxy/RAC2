import time                         # Štoparica
import matplotlib.pyplot as plt     # Risanje grafov
import random                       # Za generiranje primerov

import zabica

def izmeri_cas(fun, primer):
    """Izmeri čas izvajanja funkcije `fun` pri argumentu `primer`."""
    zacetni = time.perf_counter()
    fun(primer)
    koncni = time.perf_counter() - zacetni
    return koncni

def oceni_potreben_cas(fun, gen_primerov, n, k):
    """ Funkcija oceni potreben čas za izvedbo funkcije `fun` na primerih
    dolžine `n`. Za oceno generira primere primerne dolžine s klicom
    `gen_primerov(n)`, in vzame povprečje časa za `k` primerov. """
    vsota = 0
    for _ in range(k):
        primer = gen_primerov(n)
        vsota += izmeri_cas(fun, primer)
    return vsota / k

def test_gen_sez(n):
    "Generira testni seznam dolžine n."
    return [random.randint(1, n) for _ in range(n)]

def primerjaj_case_dveh(fun1, fun2, gen_primerov, sez_n, ime , k=10):
    """ Funkcija izpiše tabeli časa za izračun 'fun1' in 'fun2' na primerih generiranih z
    'gen_primerov' glede na velikosti primerov v 'sez_n'. Za oceno uporabi 'k' ponovitev in 
    izriše grafa obeh funkcij. """
    # Seznama časov, ki jih želimo tabelirati
    casiFun1 = []
    casiFun2 = []

    for n in sez_n:
        casiFun1.append(oceni_potreben_cas(fun1, gen_primerov, n, k))
        casiFun2.append(oceni_potreben_cas(fun2, gen_primerov, n, k))
    
    vel1 = len(max([str(cas) for cas in casiFun1], key = len))
    vel2 = len(max([str(cas) for cas in casiFun1], key = len))
    pad = max(vel1, vel2)

    # izpiši glavo tabele
    print(str('n').ljust(20, ' ') +  '| ' + str('Čas izvedbe[s](fun1)').ljust(40, ' ') + '| ' + str('Čas izvedbe[s](fun2)').ljust(40, ' '))

    # horizontalni separator
    sep_len = len(str(max(casiFun1))) + len(str(max(casiFun2))) + pad + 20 
    print("-"*sep_len)

    # izpiši vrstice
    for i in range(len(sez_n)):
        razmik1 = ' ' *(pad - len(str(sez_n[i])) +1)
        print(str(sez_n[i]).ljust(20, ' ') +  '| ' + str(casiFun1[i]).ljust(40, ' ') + '| ' + str(casiFun2[i]).ljust(40, ' '))
        
    #Izris grafa.
    plt.grid(linestyle = '-', linewidth = 0.5)
    plt.plot(sez_n, casiFun1, label = 'Zabica Bellman')        
    plt.plot(sez_n, casiFun2, label = 'zabica iterativno') 
    plt.legend()
    plt.xlabel('Velikost problema.')
    plt.ylabel('Potreben čas [s]')
    plt.title('Primerjava časovne zahtevnosti dveh funkcij.')
    plt.savefig(ime + '.jpg')
    plt.show()


if __name__ == '__main__':
    print("ZAČENJAM")
    primerjaj_case_dveh(zabica.zabica, zabica.zabica_iterativno, test_gen_sez, [i for i in range(20)], "primerjava")
    print("KONEC")