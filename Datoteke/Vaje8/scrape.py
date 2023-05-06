# with open("C:\\Users\\grego\\Desktop\\FAKS\\3.letnik\\Racunalnistvo 2\\Porocila\\Drugo\\Vaje8\\roadNet-TX.txt",'r') as file:
#         tocke = list()
#         for vrstica in file:
#             # če je vrstica začetna, ki nas ne zanima, jo spusti
#             if '#' in vrstica:
#                 continue
#             else:
#                 zacetek, konec = vrstica[:-1].split('\t')  # povezava
#                 tocke.append((int(zacetek), int(konec)))
#         tocke = sorted(tocke, key=lambda x: x[0])  # uredimo tabelo povezav
#         print(tocke)




# def seznam_povezav(ime_dat):
#     '''Iz dane txt datoteke razbere povezave grafa, povezave doda v seznam `tocke` in jih uredi glede na začetna vozlišča.'''
#     tocke = list()
#     with open(ime_dat, 'r') as file:
#         for vrstica in file:
#             # če je vrstica začetna, ki nas ne zanima, jo spusti
#             if '#' in vrstica:
#                 continue
#             else:
#                 zacetek, konec = vrstica[:-1].split('\t')  # povezava
#                 tocke.append((int(zacetek), int(konec)))
#     tocke = sorted(tocke, key=lambda x: x[0])  # uredimo tabelo povezav
#     return tocke  # [(0, 1), (0, 2), (0, 29), (1, 0), (1, 23), (1, 32), (2, 0), (2, 26),...], integer
        
# def ustvari_graf(povezave):
#     graf = [list() for _ in range(povezave[-1][0]+1)]
#     i = 0
#     for tocka in povezave:
#         if tocka[0] == i:
#             graf[i].append((tocka[1], 1))
#         else:
#             i +=1
#             graf[i].append((tocka[1], 1))
#     return graf



# def razberi(file):
#     edges = list()
#     n = 0
#     with open(file, 'r') as f:
#         lines = f.readlines()
#         for line in lines:
#             if line[0] == '#':
#                 continue
#             u, v = map(int, line.strip().split('\t'))
#             n = max(n, u, v)
#             edges.append((u,v))
#     edges = sorted(edges, key=lambda x: x[0])
#     return n, edges
    


#tab= seznam_povezav('roadNet-TX.txt')
#n, edges = razberi('roadNet-TX.txt')


def Bellman_Ford(graf, zacetek, n):
    # n = stevilo vozlisc
    razdalje = [float('Inf')]*n
    razdalje[zacetek] = 0
    
    for _ in range(n-1):  # st. operacij je za 1 manj kot je vozlisc
        for u, v, w in graf:
            # u = začetek
            # v = konec
            # w = utež na povezavi (u,v)
            if razdalje[u] != float('Inf') and razdalje[u] + w < razdalje[v]:
                # našli smo bližnjico
                razdalje[v] = razdalje[u] + w
                
    # Preverimo ali ima graf negativen cikel
    for u, v, w in graf:
        if razdalje[u] != float('Inf') and razdalje[u] + w < razdalje[v]:
            return None
        
    return razdalje


g = [(0, 1, 2),
    (0, 2, 4),
    (1, 3, 2),
    (2, 4, 3),
    (2, 3, 4),
    (4, 3, -5)]

sez_razdalj = Bellman_Ford(g, 0, 5)
print(sez_razdalj)

def zapisi_txt(ime, graf):
    '''
        Zapiše graf v txt datoteko pod imenom ime.txt. Vrstice
        so v obliki `u v w(u,v)`, kjer je (u,v) povezava in w(u,v) njena utež.
        u je začetno in v končno vozlišče povezave.
    '''
    with open(ime + '.txt', 'w') as dat:
        for u, v, w in graf:
            vrstica = '{} {} {}\n'
            dat.write(vrstica.format(u, v, w))
zapisi_txt('BF',g)


import random

def generiraj_graf(n):
    '''
        Zgenerira in vrne graf kot seznam sosedov za število vozlišč od 0 do n.
        Torej n+1 vozlišč. Uteži so cela števila od 1 do 10.
    '''
    graf=list()
    for vozlisce in range(n+1):
        tab = list()  # tabela sosedov i-tega vozlisca
        for sosed in range(random.randint(1,n+1)):  # vsako vozlišče ima vsaj enega soseda
            tab.append((random.randint(0,n), random.randint(1,10)))  # (sosed, utež)
        graf.append(tab)
    return graf




from collections import deque

from collections import deque  # double ended queue

def BFS_poti(G, u):
    '''Vrne najkrajše poti v neuteženem grafu G od u do vseh ostalih vozlišč.
        Graf G je predstavljen kot seznam sosedov.
    '''
    n = len(G)
    d = [-1]*n  # vse razdalje na začetku nastavimo na 0
    obiskani = [False]*n
    poti = [-1] * n  # drevo najkrajših poti od u do vseh vozlišč
    q = deque([(u, 0)])  # drugi element=0 je razdalja i-tega vozlišča do u
    while q:
        trenutni, razdalja = q.popleft() # vzamemo in odstranimo vozlišče z leve strani vrste
        if obiskani[trenutni]:
            continue
        else:
            obiskani[trenutni] = True
            d[trenutni] = razdalja
            for sosed in G[trenutni]:
                if not obiskani[sosed]:
                    # soseda dodamo na desno stran vrste
                    #q += [(sosed, razdalja + 1)]
                    q.append((sosed, razdalja+1)) # dodamo soseda na desno stran vrste
                    if poti[sosed] == -1:
                        poti[sosed] = trenutni
    poti[u] = u
    return d, poti

def ustvari_graf(datoteka):
    """
    Funkcija prejme ime tekstovne datoteke, ki vsebuje usmerjene povezave in iz nje ustvari neutežen graf z usmerjenimi povezavami, predstavljen kot seznam sosednosti.
    """
    with open(datoteka, 'r') as file:
        # prve 4 vrstice ne porebujemo, jih samo preberemo
        for _ in range(4):
            file.readline()
        
        # napolnemo seznam povezav s povezavami iz datoteke roadNET-TX.txt
        sez_povezav = []
        for vrstica in file:
            vrstica = vrstica.strip().split('\t')
            sez_povezav.append((int(vrstica[0]), int(vrstica[1])))

        # uredimo vozlišča po velikosti, da dobimo največje vozlišče, saj bo 
        # naš graf G, predstavljen kot seznam sosednosti, vseboval n+1 povezav
        sez_povezav.sort(key=lambda x: x[0], reverse=True)
        n = sez_povezav[0][0]

        # Ustvarimo seznam sosednosti, kjer so povezave usmerjene, uteži pa enake 1
        G = [[] for _ in range(n+1)]
        for povezava in sez_povezav:
            u = povezava[0]
            v = povezava[1]
            G[u].append((v, 1))
    return G


def ustvari_neutezen_graf(povezave):
    graf = [list() for _ in range(povezave[-1][0]+1)]
    i = 0
    for tocka in povezave:
        if tocka[0] == i:
            graf[i].append(tocka[1])
        else:
            i +=1
            graf[i].append(tocka[1])
    return graf  #[[1, 2, 29], [0, 23, 32], ...]


G1 = [
    [(1,1), (5,1)],
    [(3, 1), (4, 1), (5, 1)],
    [(4,1), (5, 1)],
    [(5,1), (2, 1)],
    [(4,1), (5, 1)],
    [(0, 1), (1,1), (4, 1)]
]

G2_neutezen = [
    [1, 5],
    [3, 4, 5],
    [4, 5],
    [5, 2],
    [4, 5],
    [0, 1, 4]
]


import heapq
from collections import deque

def Dijkstra_Mod(G, s, t):
    """
    Funkcija sprejme usmerjen in utežen graf G predstavljen
    s seznamom sosednosti ter začetno vozlišče s.
    Torej G[i] = [(v_1, w_1), ... (v_d, w_d)],
    kjer je (i, v_k) povezava v grafu z utežjo w_k.
    Vrne najkrajšo pot od vozlišča s do vseh ostalih (shranjena v seznamu razdaljeDo).
    Vrne tudi seznam poti, ki predstavlja drevo najkrajših poti od s do vseh ostalih vozlišč.
    Poleg tega sprejme tudi končno vozlišče t in vrne najcenejšo razdaljo od s do t. Prav tako vrne drevo najkraših poti kot seznam, kjer
    je i-ti element oče vozlišča i-1.
    """
    n = len(G)
    
    # Nastavimo začetne vrednosti
    obiskani = [False] * n
    razdaljeDo = [-1] * n
    poti = [None] * n

    # Na vrsto dodamo trojico (d, v, p), kjer je:
    # v vozlišče, d razdalja do njega, p pa prejšnje vozlišče na najkrajši poti od
    # s do v.
    Q = [(0, s, s)]

    while Q:
        
        # Vzamemo minimalen element iz vrste
        # heapq.heappop(Q) odstrani element iz seznama Q, ter pri tem ohranja
        # lastnost kopice : seznam Q tretira kot dvojiško drevo!
        razdalja, u, p = heapq.heappop(Q)

        # če je že obiskan, nadaljujemo.
        if obiskani[u]:
            continue
        
        # obiščemo vozlišče ter nastavimo njegovo razdaljo
        # ter predhodnika na najkrajši poti od s do u
        obiskani[u] = True
        razdaljeDo[u] = razdalja
        poti[u] = p

        # če smo prišli do vozlišča s, skonstruiramo drevo poti
        # in vrnemo najcenejšo razdaljo od s do t
        if u == t:
            pot_do_t = [t]
            pred = poti[t]
            while pred != s:
                pot_do_t.append(pred)
                pred = poti[pred]
            pot_do_t.append(s)
            return razdaljeDo[t], pot_do_t
        
        # gremo čez vse sosede in dodamo potrebne elemente na vrsto.
        for (v, teza) in G[u]:
            if not obiskani[v]:

                # heap.heappush(Q, elem) doda element v seznam Q, kjer ohranja lastnost kopice.
                heapq.heappush(Q, (razdalja + teza, v, u))

    return razdaljeDo, poti


tab = ("C:\\Users\\grego\\Desktop\\FAKS\\3.letnik\\Racunalnistvo 2\\Porocila\\Drugo\\Vaje8\\roadNet-TX.txt")
graf2 = ustvari_graf(tab)
razdalje, poti = Dijkstra_Mod(graf2, 100)
graf_neutezen = ustvari_neutezen_graf(tab)
razdalje2, poti2 = BFS(graf_neutezen, 100)
print(razdalje == razdalje2)
