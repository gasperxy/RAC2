import matplotlib.pyplot as plt
import random
import time
import heapq  # kopica
from collections import deque

def djikstra(G, s):
    """
    Funkcija sprejme usmerjen in utežen graf G predstavljen
    s seznamom sosednosti ter začetno vozlišče s.
    Torej G[i] = [(v_1, w_1), ... (v_d, w_d)],
    kjer je (i, v_k) povezava v grafu z utežjo w_k.
    Vrne seznam razdaljeDo, ki predstavlja najkrajšo pot od vozlišča s
    do vseh ostalih.
    Vrne tudi seznam poti, ki predstavlja drevo najkrajših poti od s
    do vseh ostalih vozlišč.
    """
    n = len(G)
    if n != 0:
        # Nastavimo začetne vrednosti za sezname obiskani, razdaljaDo in poti.
        obiskani = [False] * n
        razdaljeDo = [-1] * n
        poti = [-1] * n
        # Na vrsto dodamo trojico (d, v, p), kjer je:
        # v vozlišče, d razdalja do njega, p pa prejšnje vozlišče na najkrajši poti od
        # s do v.
        Q = [(0, s, s)]

        while Q:
        
            # Vzamemo minimalen element iz vrste
            # heapq.heappop(Q) odstrani element iz seznama  Q, ter pri tem ohranja
            # lastnost kopice : seznam Q tretira kot dvojiško drevo!
            razdalja, u, p = heapq.heappop(Q)  # iz seznama q vzame zadnji element, ampak ohranja lastnosti kopice

            # če je že obiskan, nadaljujemo.
            if obiskani[u]:
                continue
        
            # obiščemo vozlišče ter nastavimo njegovo razdaljo
            # ter predhodnika na najkrajši poti od s do u
            obiskani[u] = True
            razdaljeDo[u] = razdalja
            poti[u] = p

            # gremo čez vse sosede in dodamo potrebne elemente na vrsto.
            for (v, teza) in G[u]:
                if not obiskani[v]:

                    # heap.heappush(Q, elem) doda element v seznam Q, kjer ohranja lastnost kopice.
                    heapq.heappush(Q, (razdalja + teza, v, u))

        return razdaljeDo, poti
    else: return None

def BFS_poti(G, u):
    '''Vrne najkrajše poti v neuteženem grafu G od u do vseh ostalih vozlišč.
        Graf G je predstavljen kot seznam sosedov.
    '''
    n = len(G)
    if n != 0:
        d = [-1]*n  # vse razdalje na začetku nastavimo na 0
        obiskani = [False]*n
        poti = [-1] * n
        q = deque([(u, 0)])  # drugi element=0 je razdalja i-tega vozlišča do u
        while q:
            trenutni, razdalja = q.popleft()
            if obiskani[trenutni]:
                continue
            else:
                obiskani[trenutni] = True
                d[trenutni] = razdalja
                for sosed in G[trenutni]:
                    if not obiskani[sosed]:
                        # soseda dodamo na desno stran vrste
                        #q += [(sosed, razdalja + 1)]
                        q.append((sosed, razdalja+1))
                        if poti[sosed] == -1:
                            poti[sosed] = trenutni
                       
        poti[u] = u
        return d, poti
    else:
        return None

G1_neutezen = [
    [1, 5],
    [3, 4, 5],
    [4, 5],
    [5, 2],
    [4, 5],
    [0, 1, 4]]
G1 = [
    [(1,1), (5,1)],
    [(3, 1), (4, 1), (5, 1)],
    [(4,1), (5, 1)],
    [(5,1), (2, 1)],
    [(4,1), (5, 1)],
    [(0, 1), (1,1), (4, 1)]]

def izmeri_cas_poti(fun, graf, zacetno_vozlisce):
    '''Izmeri čas izvajanja funkcije `fun` pri argumentu `graf`.
    '''
    cas1 = time.perf_counter()
    fun(graf, zacetno_vozlisce)
    cas2 = time.perf_counter()
    cas = cas2 - cas1
    return cas

def gen_graf(st_vozlisc):
    '''Generira neuteženi graf `graf1` in uteženi graf `graf2` z n vozlišči kot seznam sosednosti.
        V uteženem grafu so uteži enake 1. Oba grafa sta po povezavah enaka.
    '''
    graf1 = list([] for _ in range(st_vozlisc))  # vozlišča od 0 do st_vozlisc-1
    graf2 = list([] for _ in range(st_vozlisc))  # vozlišča od 0 do st_vozlisc-1
    for i in range(st_vozlisc):
        mn = set()  # da se sosedje ne ponavljajo
        for j in range(random.randint(0, st_vozlisc-1)):  # random koliko sosedov bo imelo i-to vozlišče
            stevilo = random.randint(0, st_vozlisc-1)
            mn.add(stevilo)
        for elt in mn:
            graf1[i].append(elt)
            graf2[i].append((elt, 1))
    return graf1, graf2

def izpisi_case(tab):
    n = len(tab)
    # za lepšo poravnavo izračunamo širino levega stolpca
    pad = n
    dol = max([len(str(x)) for x in tab])
    sep_len = pad + dol + 3

    # izpiši glavo tabele
    print("{:{pad}} | Čas izvedbe [s]".format("Št. vozlišč", pad=pad))
    # horizontalni separator
    sep_len = pad + dol + 3 
    print("-"*sep_len)
    
    st = 10
    # izpiši vrstice
    for i in range(n):
        print('{:{}} | {}'.format(st, pad, tab[i]))
        st += 10

def narisi_in_pokazi_graf(tocke1, tocke2):
    x_os = [_ for _ in range(len(tocke1))]
    plt.plot(x_os, tocke1, 'r')  # BFS
    plt.plot(x_os, tocke2, 'b')  # Djikstra
    plt.savefig('graf_BFS_Djikstra.png')
    plt.show()



##################################################

tab_testov = list()  # graf1: graf2
tab_testov.append((G1_neutezen, G1))
for s in range(1, 15):
    g1, g2 = gen_graf(s*10)  # st_vozlisc = 10, 20, 30, ..., 100
    tab_testov.append((g1, g2))

casi_g1 = list()
casi_g2 = list()
for neutezeni, utezeni in tab_testov:
    cas1 = izmeri_cas_poti(BFS_poti, neutezeni, 0)
    cas2 = izmeri_cas_poti(djikstra, utezeni, 0)
    casi_g1.append(cas1)
    casi_g2.append(cas2)

print('Časi izvajanja BFS algoritma:')
izpisi_case(casi_g1)

print('Časi izvajanja Djikstra algoritma:')
izpisi_case(casi_g2)

narisi_in_pokazi_graf(casi_g1, casi_g2)



