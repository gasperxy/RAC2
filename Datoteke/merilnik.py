import time                         # Štoparica
import matplotlib.pyplot as plt     # Risanje grafov
import random                       # Za generiranje primerov

from zabica import zabica
from zabica_iterativno import zabica_iterativno



def izmeri_cas(fun, primer):
    """Izmeri čas izvajanja funkcije `fun` pri argumentu `primer`."""
    # NAMIG: klic funkcije `time.perf_counter()` vam vrne število sekund od 
    # neke točke v času. Če izmerite čas pred izračunom funkcije in čas po 
    # končanem izračunu, vam razlika časov pove čas izvajanja (funkcija je 
    # natančnejša od time.time()).
    zacetek = time.perf_counter()
    fun(primer)
    konec = time.perf_counter()
    return konec- zacetek




def oceni_potreben_cas(fun, gen_primerov, n, k):
    """ Funkcija oceni potreben čas za izvedbo funkcije `fun` na primerih
    dolžine `n`. Za oceno generira primere primerne dolžine s klicom
    `gen_primerov(n)`, in vzame povprečje časa za `k` primerov. """

    # NAMIG: `k`-krat generirajte nov testni primer velikosti `n` s klicem
    # `gen_primerov(n)` in izračunajte povprečje časa, ki ga funkcija porabi za
    # te testne primere.
    skupni_cas = 0
    for i in range(k):
        skupni_cas += izmeri_cas(fun, gen_primerov(n))
    return skupni_cas / k



def narisi_in_pokazi_graf(fun, gen_primerov, sez_n, k=10):
    """ Funkcija nariše graf porabljenega časa za izračun `fun` na primerih
    generiranih z `gen_primerov`, glede na velikosti primerov v `sez_n`. Za
    oceno uporabi `k` ponovitev. """

    # NAMIG: preprost graf lahko narišemo z `plt.plot(sez_x, sez_y, 'r')`, ki z
    # rdečo črto poveže točke, ki jih definirata seznama `sez_x` in `sez_y`. Da
    # se graf prikaže uporabniku, uporabimo ukaz `plt.show()`. Za lepše grafe
    # si poglejte primere knjižnice [matplotlib.pyplot] (ki smo jo preimenovali
    # v `plt`).

    sez_x, sez_y = [], []
    for el in sez_n:
        sez_x.append(el)
        sez_y.append(oceni_potreben_cas(fun, gen_primerov, el, k))

    plt.grid(linestyle = '-', linewidth = 0.5)
    plt.xlabel('Velikost problema')
    plt.ylabel('Potreben čas [s]')
    plt.plot(sez_x, sez_y, 'r')
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


def izpisi_case(fun, gen_primerov, sez_n, k=10):
    """ Funkcija izpiše tabelo časa za izračun `fun` na primerih generiranih z
    `gen_primerov`, glede na velikosti primerov v `sez_n`. Za oceno uporabi `k`
    ponovitev. """
    tab = []
    for i in sez_n:
        primer = gen_primerov(i)
        trenutni = izmeri_cas(fun,primer)
        tab.append(trenutni)

    # Seznam časov, ki jih želimo tabelirati
    casi = tab # DOPOLNITE KODO

    # za lepšo poravnavo izračunamo širino levega stolpca
    pad = len(max(str(sez_n)))  # DOPOLNITE KODO

    # izpiši glavo tabele
    """ POJASNILO: če uporabimo `{:n}` za f-niz, bo metoda vstavila
    argument, in nato na desno dopolnila presledke, dokler ni skupna dolžina
    niza enaka vrednosti `n`. Če želimo širino prilagoditi glede na neko
    spremenljivko, to storimo kot prikazuje spodnja vrstica (torej s
    `{:{pad}}` kjer moramo nato podati vrednost za `pad`)."""
    print("{:{pad}} | Čas izvedbe [s]".format("n", pad=pad))
    # horizontalni separator

    sep_len = pad + 3 + len(str(max(tab)))  # DOPOLNITE KODO (črta naj bo široka kot najširša vrstica)
    print("-"*sep_len)
    for i in range(len(sez_n)):
        razmik = ' '*(pad - len(str(sez_n[i]))+1)
        print(str(sez_n[i]) + razmik + '| ' + str(casi[i]))
    # izpiši vrstice
    # DOPOLNITE KODO

    # končna tabela naj izgleda približno takole (seveda pa jo lahko polepšate):
    # n  | Čas izvedbe [s]
    # ---------------------------
    # 10 | 4.198900114715798e-06 
    # 20 | 1.6393299847550225e-05
    # 30 | 3.7693600006605266e-05

def test_gen_sez(n):
    """Generira testni seznam dolžine n."""
    return [random.randint(1, n) for _ in range(n)]


# -----------------------------------------------------------------------------
# Ker je datoteka mišljena kot knjižnica, imejte vse 'primere izvajanja'
# zavarovane z `if __name__ == '__main__':`, da se izvedejo zgolj če datoteko
# poženemo in se ne izvedejo če datoteko uvozimo kot knjižnico

if __name__ == '__main__':
    #izpisi_case(zabica, test_gen_sez, [n for n in range(1, 50)])
    #izpisi_case(zabica_iterativno, test_gen_sez, [n for n in range(50)])
    narisi_in_pokazi_vec_funkcij([(zabica_iterativno, "red"), (zabica, "blue")], test_gen_sez, [n for n in range(1, 30)])