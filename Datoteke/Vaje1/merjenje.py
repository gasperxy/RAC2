import matplotlib.pyplot as plt
import time  
import random   

def zabica(mocvara):
    """Dinamično izračuna število potrebnih skokov, da žabica zapusti močvaro."""
    def skaci(i,e):
        if i >= len(mocvara):
            return 0
        if (i,e) in memo:
            return memo[(i,e)]
        nova_energija = e + mocvara[i] 
        min_skokov = min(skaci(i+k, nova_energija-k) for k in range(1, nova_energija+1))
        memo[(i,e)] = 1 + min_skokov
        return memo[(i,e)]

    memo = {}
    return skaci(0,0)

def zabica_iterativno(mocvara):
    """Iterativno izračuna najmanjše število potrebnih skokov, da žabica zapusti močvaro."""
    n = len(mocvara)
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[n][i] = 0
        dp[n - 1][i] = 1

    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            m = n
            e = j
            e += mocvara[i]

            if i + j > n:
                dp[i][j] = 1
                continue

            for d in range(1, e + 1):
                if i + d >= n:
                    m = 0
                else:
                    if e - d >= n:
                        m = 1
                    else:
                        m = min(m, dp[i + d][e - d])
            dp[i][j] = 1 + m
    return dp[0][0]


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

def primerjava_urejanj(fun1, fun2, gen, sez_n, k, shrani = False):
    """Nariše dva grafa za primerjanje dveh funkcij."""
    sez_x = sez_n
    sez_y1 = [oceni_potreben_cas(fun1, gen, n, k) for n in sez_n]
    sez_y2 = [oceni_potreben_cas(fun2, gen, n, k) for n in sez_n]
    plt.plot(sez_x, sez_y1, 'r')
    plt.plot(sez_x, sez_y2, 'b')
    plt.xlabel("Velikost problema")
    plt.ylabel("Potreben čas [s]")
    if shrani:
        plt.savefig("dve_funkciji_primerjava.png")
    plt.show()

def narisi_in_pokazi_graf(fun, gen_primerov, sez_n, k, shrani = False):
    """ Funkcija nariše graf porabljenega časa za izračun `fun` na primerih
    generiranih z `gen_primerov`, glede na velikosti primerov v `sez_n`. Za
    oceno uporabi `k` ponovitev. """
    sez_x = sez_n
    sez_y = [oceni_potreben_cas(fun, gen_primerov, n, k) for n in sez_n]
    plt.plot(sez_x, sez_y, 'r')
    plt.xlabel("Velikost problema")
    plt.ylabel("Potreben čas [s]")
    if shrani:
        plt.savefig("casovna_zahtevnost.png")
    plt.show()

def test_gen_sez_pozitivna(n):
    "Generira testni seznam dolžine n."
    return [random.randint(1, n) for _ in range(n)]

# IZRIS GRAFOV
primerjava_urejanj(zabica, zabica_iterativno, test_gen_sez_pozitivna, [i for i in range(30)], 20, True)
narisi_in_pokazi_graf(zabica_iterativno, test_gen_sez_pozitivna, [i for i in range(70)], 10, True)
narisi_in_pokazi_graf(zabica, test_gen_sez_pozitivna, [i for i in range(70)], 10, True)