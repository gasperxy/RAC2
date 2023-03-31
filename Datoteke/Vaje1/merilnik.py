import time                         # Štoparica
import matplotlib.pyplot as plt     # Risanje grafov
from zabica import zabica
from zabica_iteracija import zabica_iteracija

def oceni_potreben_cas(fun, tab, k = 10):
    cas_zac = time.perf_counter()
    for _ in range(k):
        fun(tab)
    cas_konec = time.perf_counter()
    return (cas_konec - cas_zac) / k

def narisi_in_pokazi_vec_funkcij(tab_fun, sez_n, k = 10):
    for fun, color in tab_fun:
        sez_x = []
        sez_y = []
        for el in sez_n:
            sez_x.append(len(el))
            sez_y.append(oceni_potreben_cas(fun, el, k))
        plt.plot(sez_x, sez_y, color = color)
    plt.xlabel("Velikost problema")
    plt.ylabel("Čas [s]")
    plt.legend()
    plt.grid()
    plt.show()

# -----------------------------------------------------------------------------

if __name__ == '__main__':
    # izpisi_case(zabica, test_gen_sez, [n for n in range(1, 42)])
    # izpisi_case(zabica_iteracija, test_gen_sez, [n for n in range(42)])
    sez_1 =  [2, 4, 1, 2, 1, 3, 1]
    sez_2 = [4, 1, 8, 2, 11, 1, 1, 1, 1, 1, 2, 1]
    sez_3 = [2, 3, 1, 1, 3, 4, 1, 2, 1, 2, 2, 3, 1, 1, 2, 6, 2, 1, 1]
    sez_4 = [1, 5, 1, 1, 1, 1, 2, 2, 1, 1, 2, 3, 2, 1, 3, 2, 1, 5, 2, 2, 3, 1, 2, 3, 2, 1, 2, 3, 4]
    sez_problemov = [sez_1, sez_2, sez_3, sez_4]
    narisi_in_pokazi_vec_funkcij([(zabica_iteracija, "red"), (zabica, "green")], sez_problemov)