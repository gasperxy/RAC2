import time                         # Štoparica
import Zabica
import matplotlib.pyplot as plt     # Risanje grafov
import random                       # Za generiranje primerov


def izmeri_cas(fun, primer):
    """Izmeri čas izvajanja funkcije `fun` pri argumentu `primer`."""
    # NAMIG: klic funkcije `time.perf_counter()` vam vrne število sekund od 
    # neke točke v času. Če izmerite čas pred izračunom funkcije in čas po 
    # končanem izračunu, vam razlika časov pove čas izvajanja (funkcija je 
    # natančnejša od time.time()).
    stevec = time.perf_counter()
    fun(primer)
    stevec = time.perf_counter() - stevec
    return stevec


def oceni_potreben_cas(fun, gen_primerov, n, k):
    """ Funkcija oceni potreben čas za izvedbo funkcije `fun` na primerih
    dolžine `n`. Za oceno generira primere primerne dolžine s klicom
    `gen_primerov(n)`, in vzame povprečje časa za `k` primerov. """
    povprecje = 0
    for i in range(k):
        povprecje = izmeri_cas(fun, gen_primerov(n))
    return povprecje / k




def narisi_in_pokazi_graf(fun, gen_primerov, sez_n, k=10):
    """ Funkcija nariše graf porabljenega časa za izračun `fun` na primerih
    generiranih z `gen_primerov`, glede na velikosti primerov v `sez_n`. Za
    oceno uporabi `k` ponovitev. """

    # NAMIG: preprost graf lahko narišemo z `plt.plot(sez_x, sez_y, 'r')`, ki z
    # rdečo črto poveže točke, ki jih definirata seznama `sez_x` in `sez_y`. Da
    # se graf prikaže uporabniku, uporabimo ukaz `plt.show()`. Za lepše grafe
    # si poglejte primere knjižnice [matplotlib.pyplot] (ki smo jo preimenovali
    # v `plt`).
    cas = []
    for n in sez_n:
        cas.append(oceni_potreben_cas(fun, gen_primerov, n, k))
    plt.plot(cas, sez_n, 'r')
    plt.xlabel('Velikost problema.')
    plt.ylabel('Potreben čas [s]')
    plt.show()

def izpisi_case(fun, gen_primerov, sez_n, k=10):
    """ Funkcija izpiše tabelo časa za izračun `fun` na primerih generiranih z
    `gen_primerov`, glede na velikosti primerov v `sez_n`. Za oceno uporabi `k`
    ponovitev. """

    casi = []
    for n in sez_n:
        casi.append(oceni_potreben_cas(fun, gen_primerov, n, k))

    pad = len(max([str(cas) for cas in casi], key = len))

    print("{:{pad}} | Čas izvedbe [s]".format("n", pad=pad))
    # horizontalni separator
    sep_len = pad + len(max([str(n) for n in sez_n], key = len))
    print("-"*sep_len)

    for i in range(len(sez_n)):
        print(f"{sez_n[i]} | {casi[i]}")

    
def primerjava_algoritmov(fun, gen_primerov, sez_n, k = 10):
    '''funkcija nariše graf večih algoritmov. Funkcije morajo biti
        v tabeli.'''
    barve = ['r', 'b', 'g']
    for f in fun:
        cas = []
        for n in sez_n:
            cas.append(oceni_potreben_cas(f, gen_primerov, n, k))
        plt.plot(sez_n, cas, barve[random.randint(0, 2)])
    plt.xlabel('Velikost problema [n]')
    plt.ylabel('Potreben čas [s]')
    plt.show()

def test_gen_sez(n):
    "Generira testni seznam dolžine n."
    return [random.randint(1, 4) for _ in range(n)]
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    print("Starting")
    #primerjava iterativne zabice in zabice z rekurzijo
    primerjava_algoritmov([Zabica.zabica, Zabica.zabica_iter], test_gen_sez, [i for i in range(100)])
    #narisi_in_pokazi_graf(Zabica.zabica_iter, test_gen_sez, [i for i in range(200)])
    print("Done")
