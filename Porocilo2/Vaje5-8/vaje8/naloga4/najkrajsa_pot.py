import heapq
from collections import deque

def izpisi_pot(poti, s, t):
    """
    Funkcija sprejme seznam poti, ki predstavlja drevo najkrajših poti
    od začetnega vozlišča do vseh ostalih vozlišč, ter začetno in končno vozlišče.
    Vrne pot od začetnega do končnega vozlišča v obliki seznama vozlišč.
    """
    # Spremenljivka path bo predstavljala pot od končnega do začetnega vozlišča.
    path = [t]

    # Sledimo predhodnikom vozlišča, dokler ne pridemo do začetnega vozlišča.
    sedanji = t
    while sedanji != s:
        sedanji = poti[sedanji]
        path.append(sedanji)

    # Pot smo gradili od konca proti začetku, zato jo je potrebno obrniti.
    return path[::-1]


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
    
    # Nastavimo začetne vrednosti za sezname obiskani, razdaljaDo in poti.
    obiskani = [False] * n
    razdaljeDo = [-1] * n
    poti = [None] * n

    # Na vrsto dodamo trojico (d, v, p), kjer je:
    # v vozlišče, d razdalja do njega, p pa prejšnje vozlišče na najkrajši poti od
    # s do v.
    Q = [(0, s, s)]

    while Q:
        
        # Vzamemo minimalen element iz vrste
        # heapq.heappop(Q) odstrani element iz seznama  Q, ter pri tem ohranja
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

        # gremo čez vse sosede in dodamo potrebne elemente na vrsto.
        for (v, teza) in G[u]:
            if not obiskani[v]:

                # heap.heappush(Q, elem) doda element v seznam Q, kjer ohranja lastnost kopice.
                heapq.heappush(Q, (razdalja + teza, v, u))

    return razdaljeDo, poti

seznam_sosedov = [[] for line in open("C:\\Users\\filip\\OneDrive\\Desktop\\vaje8\\naloga1\\roadNet-TX.txt") if line[0] != "#" or line != "" ]
with open("C:\\Users\\filip\\OneDrive\\Desktop\\vaje8\\naloga1\\roadNet-TX.txt", "r") as f:
    for line in f:
        if line[0] == "#" or line == "":
             continue
        vozlisca = line.split("\t")
        prvo_vozlisce = int(vozlisca[0].strip())
        drugo_vozlisce = int(vozlisca[1].strip())
        seznam_sosedov[prvo_vozlisce].append((drugo_vozlisce, 1))

razdalje, poti = djikstra(seznam_sosedov, 100)
s = 100
t = 100000
print(izpisi_pot(poti, s, t))