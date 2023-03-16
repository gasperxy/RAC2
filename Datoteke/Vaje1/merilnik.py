import time                         # Štoparica

import matplotlib.pyplot as plt     # Risanje grafov
import random                       # Za generiranje primerov
from zabica import zabica
from zabica_iter import zabica_iteracija

def izmeri_cas(fun, primer):
    """Izmeri čas izvajanja funkcije `fun` pri argumentu `primer`."""
    # NAMIG: klic funkcije `time.perf_counter()` vam vrne število sekund od 
    # neke točke v času. Če izmerite čas pred izračunom funkcije in čas po 
    # končanem izračunu, vam razlika časov pove čas izvajanja (funkcija je 
    # natančnejša od time.time()).
    zac = time.perf_counter()
    fun(primer)
    konec = time.perf_counter()
    return konec - zac
#raise NotImplementedError
# def fun(x):
    # return 1 + x


#print(izmeri_cas(fun,5))

def oceni_potreben_cas(fun, gen_primerov, n, k):
    """ Funkcija oceni potreben čas za izvedbo funkcije `fun` na primerih
    dolžine `n`. Za oceno generira primere primerne dolžine s klicom
    `gen_primerov(n)`, in vzame povprečje časa za `k` primerov. """
    casi = 0
    for el in range(k):
        rez = izmeri_cas(fun,gen_primerov(n))
        casi += rez

    povp = casi / k
    return povp



def narisi_in_pokazi_graf(fun, gen_primerov, sez_n, k=10):
    """ Funkcija nariše graf porabljenega časa za izračun `fun` na primerih
    generiranih z `gen_primerov`, glede na velikosti primerov v `sez_n`. Za
    oceno uporabi `k` ponovitev. """

    cas = []
    for el in sez_n:
        trenutni = oceni_potreben_cas(fun,gen_primerov,el,k)
        cas.append(trenutni)
    plt.plot(sez_n, cas, 'r')
    plt.savefig('narisi_in_pokazi_graf.png')
    plt.close()

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
    pad = len(max(str(sez_n)))  

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
    for i in range(len(casi)):
        print("{:{pad}} | {}".format(sez_n[i], casi[i] , pad=pad))
    # izpiši vrstice
    # DOPOLNITE KODO

    # končna tabela naj izgleda približno takole (seveda pa jo lahko polepšate):
    # n  | Čas izvedbe [s]
    # ---------------------------
    # 10 | 4.198900114715798e-06 
    # 20 | 1.6393299847550225e-05
    # 30 | 3.7693600006605266e-05

    raise NotImplementedError


# -----------------------------------------------------------------------------
# Nekaj hitrih testnih funkcij

def test_fun_lin(sez):
    "Testna funkcija z linearno časovno zahtevnostjo."
    x = 0
    for n in sez:
        x += n
    return x


def test_fun_kvad(sez):
    "Testna funkcija s kvadratično časovno zahtevnostjo."
    x = 0
    for n in sez:
        for n in sez:
            x += n
    return x


def test_gen_sez(n):
    "Generira testni seznam dolžine n."
    return [random.randint(-n, n) for _ in range(n)]


def ure_gen_sez(n):
    "Generiramo urejen seznam dolžine n."
    return [i for i in range(n)]

# -----------------------------------------------------------------------------
# Ker je datoteka mišljena kot knjižnica, imejte vse 'primere izvajanja'
# zavarovane z `if __name__ == '__main__':`, da se izvedejo zgolj če datoteko
# poženemo in se ne izvedejo če datoteko uvozimo kot knjižnico.

if __name__ == '__main__':
    narisi_in_pokazi_vec_funkcij([(zabica_iteracija, "red"), (zabica, "green")], test_gen_sez, [n for n in range(1, 42)])