import time                         # Štoparica
import matplotlib.pyplot as plt     # Risanje grafov
import random                       # Za generiranje primerov
from zabica import zabica
from zabica_iteracija import zabica_iteracija

def izmeri_cas(fun, primer):
    """Izmeri čas izvajanja funkcije `fun` pri argumentu `primer`."""

    cas_zac = time.perf_counter()
    fun(primer)
    cas_konec = time.perf_counter()
    return cas_konec - cas_zac

def oceni_potreben_cas(fun, gen_primerov, n, k = 10):
    """ Funkcija oceni potreben čas za izvedbo funkcije `fun` na primerih
    dolžine `n`. Za oceno generira primere primerne dolžine s klicom
    `gen_primerov(n)`, in vzame povprečje časa za `k` primerov. """

    cas_zac = time.perf_counter()
    for _ in range(k):
        fun(gen_primerov(n))
    cas_konec = time.perf_counter()
    return (cas_konec - cas_zac) / k

def narisi_in_pokazi_graf(fun, gen_primerov, sez_n, k = 10):
    """ Funkcija nariše graf porabljenega časa za izračun `fun` na primerih
    generiranih z `gen_primerov`, glede na velikosti primerov v `sez_n`. Za
    oceno uporabi `k` ponovitev."""
    
    sez_x = []
    sez_y = []
    for el in sez_n:
        sez_x.append(el)
        sez_y.append(oceni_potreben_cas(fun, gen_primerov, el, k))
    plt.plot(sez_x, sez_y)
    plt.xlabel("Velikost problema")
    plt.ylabel("Čas [s]")
    plt.show()

def narisi_in_pokazi_vec_funkcij(tab_fun, gen_primerov, sez_n, k = 10):
    """Nariše vse funkcije v tabeli tab_fun na primerih generiranih z `gen_primerov`,
    glede na velikosti primerov v `sez_n`. Za oceno uporabi `k` ponovitev."""
    
    for fun, color in tab_fun:
        sez_x = []
        sez_y = []
        for el in sez_n:
            sez_x.append(el)
            sez_y.append(oceni_potreben_cas(fun, gen_primerov, el, k))
        plt.plot(sez_x, sez_y, color = color)
    plt.xlabel("Velikost problema")
    plt.ylabel("Čas [s]")
    plt.legend()
    plt.grid()
    plt.show()

def izpisi_case(fun, gen_primerov, sez_n, k = 10):
    """ Funkcija izpiše tabelo časa za izračun `fun` na primerih generiranih z
    `gen_primerov`, glede na velikosti primerov v `sez_n`. Za oceno uporabi `k`
    ponovitev. """
    
    # Seznam časov, ki jih želimo tabelirati
    velikost = sez_n.copy()
    casi = [oceni_potreben_cas(fun, gen_primerov, el, k) for el in velikost]

    # za lepšo poravnavo izračunamo širino levega stolpca
    pad = max(len(str(el)) for el in velikost)

    # izpiši glavo tabele
    """ POJASNILO: če uporabimo `{:n}` za f-niz, bo metoda vstavila
    argument, in nato na desno dopolnila presledke, dokler ni skupna dolžina
    niza enaka vrednosti `n`. Če želimo širino prilagoditi glede na neko
    spremenljivko, to storimo kot prikazuje spodnja vrstica (torej s
    `{:{pad}}` kjer moramo nato podati vrednost za `pad`)."""
    
    # Izpiše ime funkcije
    print("Tabela časov\n")
    
    print("{:{pad}} | Čas izvedbe [s]".format("n", pad = pad))
    # horizontalni separator
    sep_len = max(len(str(el)) for el in casi) + pad + 3  # DOPOLNITE KODO (črta naj bo široka kot najširša vrstica)
    print("-" * sep_len)

    # izpiši vrstice
    for ind in range(len(velikost)):
        print(f"{str(velikost[ind]):{pad}}" + " | " + str(casi[ind]))

def test_gen_sez(n):
    """Generira testni seznam dolžine n."""
    return [random.randint(1, n) for _ in range(n)]
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    # izpisi_case(zabica, test_gen_sez, [n for n in range(1, 42)])
    # izpisi_case(zabica_iteracija, test_gen_sez, [n for n in range(42)])
    narisi_in_pokazi_vec_funkcij([(zabica_iteracija, "red"), (zabica, "green")], test_gen_sez, [n for n in range(1, 42)])