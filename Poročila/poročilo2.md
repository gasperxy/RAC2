# Poročilo za vaje
**Ime:** Zala Duh

## Vsebina
* Vaje 5 (15.3.2023)
* Vaje 6 (22.3.2023)
* Vaje 7 (29.3.2023)
* Vaje 8 (5.4.2023)
* Vaje 9 (12.4.2023)
* Vaje 10 (19.4.2023)

# Vaje 5
**Datum**: 15.3.2023

Na vajah smo se ukvarjali z grafi. Povedali smo s katerimi podatkovnimi strukturami jih lahko predstavimo. Analizirali smo časovne in prostorske zahtevnosti.

___________________________
### **1. naloga**

Imamo graf usmerjen G=(V,E) z uteženimi povezavami. Torej imamo neko funkcijo ω:E→A, ki vsaki povezavi dodeli utež iz množice A.

Navedi nekaj možnih podatkovnih struktur za predstavitev grafa G. Navedi nekaj prednosti oz. slabosti vsake izmed njih. Ponovi tudi, kaj je v grafu pot, sprehod in cikel.


Graf lahko prestavimo na naslednje načine:

![Alt text](/Datoteke/vaje5_slika1.jpg)

Prostorska in časovna zahtevnost:

![Alt text](/Datoteke/vaje5_slika2.jpg)

### **2. naloga**

Usmerjenemu grafu G z n vozlišči, ki nima ciklov rečemu tudi DAG (directed acyclic graph). Vozlišča takega grafa lahko topološko uredimo. To pomeni, da obstaja da zaporedje vozlišč (v1,v2,…,vn), tako da ne obstaja povezava od vi do, če je j<i.

Sestavi algoritem, ki najde tako zaporedje. Namig: Katera vozlišča lahko zagotovo damo na prvo mesto v to ureditev? 

G - seznam sosednosti

```python
def topo_sort(G):
    n = len(G)
    in_deg = [0]*n #in_deg[i], št.povezav, ki kaže v i
    for i in range(n):
        for j in G[i]:
            in_deg[j] += 1
    izvori = [i for in range(n) if in_deg[i] == 0]
    while izvori:
        izvor = izvori.pop()
        rez.append(izvori)
        for sosed in G[izvor]:
            in_deg[sosed] -= 1
            if in_deg[sosed] == 0:
                izvor.append(sosed)
    return rez

```


# Vaje 6
**Datum**: 22.3.2023

Na vajah smo ponovili delovanje BFS algoritma in Floyd-Warshallowega algoritema. 
_____________
### **1. naloga**

Ponovi BFS algoritem. Modificiraj ga, tako da bo iskal najkrajše poti v neuteženem grafu.


**BFS - breadth first-search** -> začnemo z nekim vozliščem in najprej pogledamo vse sosede, potem pa še sosede sosedov.

**DFS - depth first-search** -> najprej gremo do prvega soseda in nato na prvega soseda od soseda dokler ne pridemo do konca, potem pa se postopoma vračamo.

*BFS uporabljamo za*:
- pregled grafa
- vpeto drevo/gozd v grafu, povezane komponente
- preverjanje dvodelnosti grafa
- iskanje najkrajših poti (v neuteženem grafu)

```python
from collections import deque

def BFS(G, u):  
    #G - graf kot seznam sosedov, u - začetno vozlišče
    n = len(G)
    d = [0]*n
    obiskani = [False]*n
    q = vrsta([(u,0)]) #začnemo v u, razdlaja je na začetku 0
    while q: #dokler vrsta ni prazna
        trenutni, razdalja = q.popleft()
        if obiskani[trenutni]:
            continue #soseda smo že obiskali
        obiskani[trenutni] = True
        d[trenutni] = razdalja
        for sosed in G[trenutni]:
            if not obiskani[sosed]:
                q.push((sosed, razdalja +1)) #v vrsto dodamo soseda in razdalji prištejemo ena
```

Časovna zahtevnost je $O(m+n)$, kjer m predstavlja število povezav in n število vozlišč. Imamo linearno časovno zahtevnost. 



### **2. naloga**

Ponovi Floyd-Warshallow algoritem. Kaj računa in kaj vrne? Kakšna je njegova časovna zahtevnost?

**Vhod:** 
- Graf G (utežen, tudi negativne uteži so dovoljenje)

**Izhod:** 
- Matrika $D$ dimenzije $n$ x $n$, kjer je $n$ število vozlišč (Matrika D je seznam seznamov)
- $D_j$ cena najkrajše poti med $i$-tim in $j$-tim vozliščem

**Ideja:**

$D_{i,j}(k) = min \{D_{i,j}(k-1), D_{i,k}(k-1) + D_{k,j}(k-1) \}$,

$D_{i,j}(k)$ je isto kot $D_{i,j}$, le da uporabljamo vozlišča od 1 do $k$.


**Robni pogoji:**
- $D_{i,i} (1) = 0$
- $D_{1,i}(1) = \omega_{1,i}$ ($ \omega_{1,i}$ utež povezave)

**Časovna zahtevnost:**
$O(n^3)$, ker $n$-krat množimo matriko velikosti $n$ x $n$.

### **3. naloga**
Simuliraj FW algoritem na spodnjem grafu. 
![Alt text](/Datoteke/vaje6_navodila2.png)

Najprej si narišemo tabelo velikosti $5 X 5$. Vozlišča oštevilčimo od 1 do 5. Pričnemo pri 1=5 in nato nadeljujemo z oštevilčenjem v smeri urinega kazalca. 
Nato v matriki zapišemo na pravilna mesta vrednost direktnih povezav in v primeru, da povezave med določenima vozliščama ni - potem to povzavo nastavimo na neskončno. 

Končna in začetna tabela izgledata tako:
![Alt text](/Datoteke/unnamed.jpg)

Iz prve tabele do druge pridemo s pomočjo Bellmanove enačbe, kjer za k vzamemo $k = 1,2,3,4,5$. 

Če bi dodali novo vozlišče bi morali narediti novo tabelo velikosti $6X6$.


# Vaje 7
**Datum**: 29.3.2023


### **1. naloga**
Iz prejšnjih vaj obravnavaj, kako razberemo najkrajše poti s pomočjo matrike Π, ki jo dobimo z FW algoritmom.

**Floyd Warshall:** 

$D_{i,j} = min\{D_{i,j}(k-1), D_{i,k}(k-1) + D_{k,j}(k-1)}$
                          
(*) $D_{i,j}(k-1)$

(**) $D_{i,k}(k-1) + D_{k,j}(k-1)$

$\Pi_{i,j}(k) ...$  predstavlja zadnje vozlišče na $i-j$ potI, kjer smemo vmes uporabiti samo vozlišča od 1 do $k$.


$\Pi_{i,\Pi_{j,k}(n)}(n)$

**Začetni pogoji:** $\Pi_{i,i} (0) = i$
- (*): $\Pi_{i,j} (k) = \Pi_{i,j}(k-1) \cdot \Pi_{i,G[i]}(0) = i$

- (**): $\Pi_{i,j} (k) = \Pi_{k,j}(k-1)$


**Rekonstrukcija poti:**

**Vhod:** vozlišči $i,j$, matrika  $\Pi(n)$

**Izhod:** najkrajša pot od $i$ do $j$

**Algoritem:**
```python
p = j 
pot = []
while p != i:
    pot.append(p)
    p = π[i][p]
pot.append(i)
return pot.reverse() 
```
**Časovna zahtevnost:**

$O(n)$, ker je while zanka enaka dolžini poti.


### **2. naloga**
Uteži sedaj dodamo še na vozlišča. Kako sedaj poiskati najcenejše poti?

Možne ideje:
- Prištejemo povezave, ki kažejo v to vozlišče
- Prištejemo povezave, ki kažejo ven iz vozlišča

Odločimo se glede na problem, smiselno obravnavamo začetno in končno vozlišče.

### **3. naloga**
Premisli, zakaj preprosta sprememba v FW algoritmu iz min na max ne najde nujno najdražje poti v grafu.
![Alt text](/Datoteke/vaje7naloga3.jpg)


### **4. naloga**
Na neki borzi se trgujejo valute po menjalnem tečaju, ki ga podaja tabela R velikosti n×n, kjer je n število različnih valut. Vrednost R[i][j] pove, da za a enot valute i dobimo a⋅R[i][j] enot valuje j. Ker menjalni tečaji lahko hitro spreminjajo in so odvisni od raznih parametrov se lahko zgodi, da R[i][j]⋅R[j][i]≠1.

Za primer si oglejmo naslednjo shemo: 
![Alt text](/Datoteke/vaje7naloga4.png)

Če trgujemo USD -> YEN -> EUR -> USD končamo z 1.44 USD. Tako zaporedje imenujemo arbitraža.


Sestavimo graf $G(V,E)$, kjer so:

- vozlišča: ($EUR$,$USD$,$YEN$)
- povezave: pretvorbe

Na tem grafu nas zanima ''najdražja pot'' od vozlišča $i$ do vozlišča $j$.  To ceno poti bomo dobili kot produkt uteži na povezavah.  Utež na povezavah $i-j$ nastavimo na $-log(R_{i,j})$ --> iščemo najcenejšo pot od $i-j$ v tem grafu.

V ta namen želimo uporabiti Floyd Warshallov algoritem (to lahko naredimo, če graf nima negativnih ciklov).

Pokažimo, da jih naš graf res nima:

**DOKAZ S PROTISLOVJEM:**

Predpostavimo, da imamo negativen cikel od $i$ do $j$.
Cena tega cikla je: 

$-(\sum_{j=1}^{k}log(R(i_{j-1},ij))) < 0 $  (pomnožimo enačbo z -1),

$-log(\Pi_{j=1}^{k} R(i_{j-1},ij)) < 0 / \cdot(-1)$ 

$log(\Pi_{j=1}^{k} R(i_{j-1},ij)) > 0$ (in dobimo)

$\Pi_{j=1}^{k} R(i_{j-1},ij)) > 1 $ 

Kar smo dobili je **arbitraža** in prišli smo do protislovja.





### **5. naloga**
Ponovi Djikstrov algoritem. Kaj so vhodni in izhodni podatki, kakšne so predpostavk, itd.

Zapiši tudi njegovo glavno idejo oziroma kar psevdo kodo.

Vhodni podatki:
* Usmerjen graf $G(V,e)$
* začetno vozlišče $s \in V$
* $c_{i,j} \geq 0 $, cene so pozitivne

Izhodni podatki:
* cene najcenejših poti od $s$ do $i$ $\forall i \in V$ --> D
* drevo najkrajših poti od $s$ do $i$ $\forall i \in V$ --> P

Cene povezav so nengativne.
```python
def dijkstra(G,s):
    n = len(G)
    D = [float("inf")] * n
    P = [None] * n
    D[s] = 0 
    P[s] = s
    obiskani = [False] * n
    q = Vrsta(V(G)) #v vrsto dodamo vozlišča
    while len(obiskani) != n:
        c = q.popmin()  # minimalni element iz vrste
        obiskani.add(c)
        for sosed, utez in G[c]:
            if sosed not in obiskani:
                if D[c] + utez + D[sosed]:
                    D[sosed] = D[c] + utez
                    P[sosed] = c
    return D,P
```

**Časovna zatevnost:**   $O(n^2)$ 




# Vaje 8
**Datum**: 5.4.2023


### **1. naloga**
Vaša naloga bo, da uporabite ta algoritem na teh podatkih, torej:

- roadNet-TX.txt spremenite v ustrezno podatkovno strukturo grafa.

```python
def pretvori_v_seznam(datoteka):
    '''Funkcija prebere datoteko in v seznam shrani vse povezave'''
    seznam = []
    with open(datoteka, 'r') as file:
        for vrstica in file:
            if vrstica[0] == '#': continue
            else:
                podatki = vrstica.split('\t')
                seznam.append((int(podatki[0]), int(podatki[1])))
    seznam.sort(key=lambda x: x[0], reverse=True)           
    return seznam

povezave = pretvori_v_seznam('roadNet-TX.txt')

def ustvari_graf(povezave):
    '''Funkcija naredi seznam sosednosti'''
    G = [list() for _ in range(povezave[0][0]+1)]
    for i in povezave:
        u,v = i[0],i[1]
        G[u].append((v, 1)) #uteži so enake 1
    return G

graf = ustvari_graf(povezave)
```
Od tu naprej si pomagamo z dijkstra algortimom, ki je definirian na sledeč način:
```python
import heapq
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

```
- **Poiščete najkrajše razdalje od vozlišča 100 do vseh ostalih**.
Če želimo najkrajše razdalje uporabimo funkcijo dijkstra na našem grafu in izberemo vozlišče 100.

```python
razdalje, poti = djikstra(G, 100)
```

- **Koliko je razdalja dG(100,100000)?**
```python
print(razdalje[100000])
#Rezultat je 240
```
- **Katero vozlišče je najbolj oddaljeno od vozlišča 100?**
```python
print(razdalje.index(max(razdalje)))
#Rezultat je vozlišče 1389039
```
- **Koliko vozlišč je dosegljivih iz vozlišča 100?**
```python
print(len(graf[100]))
#Rezultat je 2
```
### **2. naloga**
Glede na to, da graf ni utežen, lahko za isto nalogo implementiramo BFS algoritem. Implementiraj BFS algoritem, ki bo poiskal dolžine najkrajših poti od s do vseh ostalih vozlišč. Vrne naj tudi drevo najkrajših poti, tako kot Djikstra. Preveri iste zadeve kot zgoraj, dobiti moraš seveda iste odgovore.
```python
def BFS(G, u):
    '''Funkcija vrne seznam poti od vozlisca u do vseh ostalih vozlic v grafu G'''
    n = len(G)
    razdalje = [0]*n
    obiskani = [False]*n
    q = ([(u,0,u)]) #začnemo v u, razdlaja je na začetku 0
    poti =[None]*n
    while q: #dokler vrsta ni prazna
        trenutni, razdalja, prejsni = q.pop(0)
        if obiskani[trenutni]:
            continue #soseda smo že obiskali
        obiskani[trenutni] = True
        razdalje[trenutni] = razdalja
        poti[trenutni] = prejsni
        for sosed, teza in G[trenutni]:
            if not obiskani[sosed]:
                q.append((sosed, razdalja +1, trenutni)) #v vrsto dodamo soseda,razdalji prištejemo ena
    return razdalje, poti
```
```python
razdalje, poti = BFS(graf, 100)

print(razdalje)
#Rezultat 240

print(razdalje.index(max(razdalje)))
#Rezultat je vozlišče 1389039

print(len(graf[100]))
#Rezultat je 2
```

### **3. naloga**
Oba algoritma dodelaj, tako da dodaš nov vhodni podatek t, ki predstavlja končno vozlišče. Algoritma naj torej vrneta razdaljo med s in t v grafu ter pote (kot drevo) med njima. Delujeta naj, tako da se ustavita takoj ko najdemo željeno pot.
```python
def djikstra_dodelan(G, s, t):
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

        if u == t: #V primeru da je u naše željeno končno vozlišče zaključimo s to zanko in končamo
            break

        # gremo čez vse sosede in dodamo potrebne elemente na vrsto.
        for (v, teza) in G[u]:
            if not obiskani[v]:

                # heap.heappush(Q, elem) doda element v seznam Q, kjer ohranja lastnost kopice.
                heapq.heappush(Q, (razdalja + teza, v, u))

    return razdaljeDo, poti
```
```python
def BFS_dodelan(G, u, t):
    '''Funkcija vrne seznam poti od vozlisca u do vozlišča t v grafu G'''
    n = len(G)
    razdalje = [0]*n
    obiskani = [False]*n
    q = ([(u,0,u)]) #začnemo v u, razdlaja je na začetku 0
    poti =[None]*n
    while q: #dokler vrsta ni prazna
        trenutni, razdalja, prejsni = q.pop(0)
        if obiskani[trenutni]:
            continue #soseda smo že obiskali

        if trenutni == t:
            break 
        #v primeru da smo prišli do našega željenga končnega vozlišča t zaključimo s to zanko
        obiskani[trenutni] = True
        razdalje[trenutni] = razdalja
        poti[trenutni] = prejsni
        for sosed, teza in G[trenutni]:
            if not obiskani[sosed]:
                q.append((sosed, razdalja +1, trenutni)) #v vrsto dodamo soseda,razdalji prištejemo ena
    return razdalje, poti
```
### **4. naloga**
Zapiši funkcijo, ki sprejme začetno vozlišče s, končno vozlišče t ter drevo najkrajših poti ter vrne najkrajšo pot med njima v obliki seznama.

Sedaj rekonstruiraj najkrajšo pot med vozliščem 100 in 100000.
```python
def pot_iz_s_v_t(s, t, drevo):
    seznam = list()
    while t != s: 
        seznam.append(t) 
        t = drevo[t]
    seznam.append(s)
    return seznam
```
```python
razdalje, poti = BFS(graf, 100)
pot = pot_iz_s_v_t(100, 100000, poti)
print(pot)
```
### **5. naloga**
Analiziraj časovne zahtevnosti algoritmov. Primerjaj hitrost med djikstro in BFS-jem. Prav tako analiziraj razliko med djikstro, ki izračuna najkrajše poti od s do vseh ostalih ter jo primerjaj z tisto verzijo iz Naloge 3.

Če nas bi zanimale najkrajše poti od s do t_1, t_2, ..., t_k, kateri algoritem bi uporabil? Probaj odgovor podat na podlagi parametra k, ter analize, ki si jo opravil.
```python
import time                         # Štoparica

import matplotlib.pyplot as plt     # Risanje grafov
import random                       # Za generiranje primerov

from djikstra import *
from bfs_algoritem import *

def pretvori_v_seznam(datoteka):
    '''Funkcija prebere datoteko in v seznam shrani vse povezave'''
    seznam = []
    with open(datoteka, 'r') as file:
        for vrstica in file:
            if vrstica[0] == '#': continue
            else:
                podatki = vrstica.split('\t')
                seznam.append((int(podatki[0]), int(podatki[1])))
    seznam.sort(key=lambda x: x[0], reverse=True)
                
    return seznam

#seznam povezav
povezave = pretvori_v_seznam('roadNet-TX.txt')

def ustvari_graf(povezave):
    '''Funkcija naredi seznam sosednosti'''
    G = [list() for _ in range(povezave[0][0]+1)]
    for i in povezave:
        u,v = i[0],i[1]
        G[u].append((v, 1)) #uteži so enake 1
    return G

#ustvarimo graf
graf = ustvari_graf(povezave)

def djikstra_dodelan(G, s, t):
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

        if u == t: #V primeru da je u naše željeno končno vozlišče zaključimo s to zanko in končamo
            break

        # gremo čez vse sosede in dodamo potrebne elemente na vrsto.
        for (v, teza) in G[u]:
            if not obiskani[v]:

                # heap.heappush(Q, elem) doda element v seznam Q, kjer ohranja lastnost kopice.
                heapq.heappush(Q, (razdalja + teza, v, u))

    return razdaljeDo, poti

def BFS_dodelan(G, u, t):
    '''Funkcija vrne seznam poti od vozlisca u do vozlišča t v grafu G'''
    n = len(G)
    razdalje = [0]*n
    obiskani = [False]*n
    q = ([(u,0,u)]) #začnemo v u, razdlaja je na začetku 0
    poti =[None]*n
    while q: #dokler vrsta ni prazna
        trenutni, razdalja, prejsni = q.pop(0)
        if obiskani[trenutni]:
            continue #soseda smo že obiskali

        if trenutni == t:
            break 
        #v primeru da smo prišli do našega željenga končnega vozlišča t zaključimo s to zanko
        obiskani[trenutni] = True
        razdalje[trenutni] = razdalja
        poti[trenutni] = prejsni
        for sosed, teza in G[trenutni]:
            if not obiskani[sosed]:
                q.append((sosed, razdalja +1, trenutni)) #v vrsto dodamo soseda,razdalji prištejemo ena
    return razdalje, poti


vozlisce = [1,10,100,1000,10000,100000,1000000]
#Dijkstra-nedodelana

casi_d1 = []
cas_d1 = 0

for i in vozlisce:
    zacetek = time.perf_counter()
    djikstra(graf,i)
    konec = time.perf_counter()
    cas_d1 += konec - zacetek
    casi_d1.append(cas_d1)

#dijkstra dodelana

casi_d2 = []
cas_d2 = 0

for i in vozlisce:
    zacetek = time.perf_counter()
    djikstra_dodelan(graf,1,i)
    konec = time.perf_counter()
    cas_d2 += konec - zacetek
    casi_d2.append(cas_d2)
    
#BFS

casi_b1 = []
cas_b1 = 0

for i in vozlisce:
    zacetek = time.perf_counter()
    BFS(graf,i)
    konec = time.perf_counter()
    cas_b1 += konec - zacetek
    casi_b1.append(cas_b1)
    
#BFS dodelan
    
casi_b2 = []
cas_b2 = 0

for i in vozlisce:
    zacetek = time.perf_counter()
    BFS_dodelan(graf,1,i)
    konec = time.perf_counter()
    cas_b2 += konec - zacetek
    casi_b2.append(cas_b2)
    
    
print(casi_d1)
print(casi_d2)
print(casi_b1)
print(casi_b2)

x_os = [1,2,3,4,5,6,7]

plt.grid(linestyle = '-', linewidth = 0.5)
plt.xlabel('Število vozlišč')
plt.ylabel('Potreben čas [s]')
plt.plot(x_os, casi_d1, label='Dijkstra - nedodelan')
plt.plot(x_os, casi_d2, label='Dijkstra - dodelan')
plt.plot(x_os, casi_b1, label='BFS - nedodelan')
plt.plot(x_os, casi_b2, label='BFS - dodelan')
plt.show()
```

![Alt text](/Datoteke/graf_8naloga.png)

# Vaje 9
**Datum**: 12.4.2023

### **1. naloga**
Nadaljujte z nalogami 2,3,4 od zadnjič. Naloga 5 naj ostane za poročilo.
### **2. naloga**
Konstruirajte nov graf, ki vsebuje le vozlišča od 0 do N.

Vsaki povezavi določite neko pozitivno utež (lahko čisto naključno) in zadevo shranite v novo .txt datoteko. Vrstice naj bodo oblike u v w(u,v), kjer je (u,v) povezava in w(u,v) njena utež.

(Koda sposojena od sošolke Diane Škof)
```python 
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


def zapisi_txt(ime, graf):
    '''
        Zapiše graf v txt datoteko pod imenom ime.txt. Vrstice
        so v obliki `u v w(u,v)`, kjer je (u,v) povezava in w(u,v) njena utež.
        u je začetno in v končno vozlišče povezave.
    '''
    with open(ime + '.txt', 'w') as dat:
        for ind, sosedje in enumerate(graf):
            for sosed in sosedje:
                vrstica = '{} {} {}\n'
                dat.write(vrstica.format(ind, sosed[0], sosed[1]))


g1 = generiraj_graf(49)  # 50 vozlišč = 0, 1, 2,... 49
zapisi_txt('graf_g1', g1)
```

### **3. naloga**
Implementiranje še Bellman-Fordov algoritem in ga poženite na grafu iz prejšnje naloge. Analiziraje kako velik N iz prejšne naloge morate vzeti, da bo algoritem še deloval v zglednem času.

(Koda sposojena od sošolke Diane Škof)
```python
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
    return razdalje

def seznam_povezav_BF(ime_dat):
    '''Iz dane txt datoteke razbere povezave grafa, povezave doda v seznam `tocke` in jih uredi glede na začetna vozlišča.'''
    tocke = list()
    with open(ime_dat, 'r') as file:
        for vrstica in file:
            zacetek, konec, utez = vrstica[:-1].split(' ')
            tocke.append((int(zacetek), int(konec), int(utez)))
    return tocke

graf = seznam_povezav_BF('graf_g1.txt')
sez_razdalj = Bellman_Ford(graf, 0, 50)
print(sez_razdalj)
```

# Vaje 10
**Datum**: 19.4.2023
### **1. naloga**
Simuliraj delovanje (min) kopice. Za vsavljanje je kot operacija število, za brisanje pa x. Za boljšo predstavo nariši kar drevesa.

Operacije: 8,2,1,3,7,6, x, x, 5, x, -3, x

![Alt text](/Datoteke/kopice.jpg)

### **2. naloga**
Predstavi kopico s seznamom in zapiši delovanje pop() in push(x) operacij.

T je seznam dolžine $n$, ta predstavlja našo kopico.

T[$i$] je $i$-to vozlišče.

Sinovi od $i$ so $2i$ in $2i+1$, če je prvi indeks v tabeli enak 1, če je prvi indeks v tabeli enak 0, sta sinova $2i+1$ in $2i+2$.

Oče je v primeru, da je prvi indeks v tabeli enak 0, na indeksu  $(i-1) // 2$. 

```python
def push(T,x):
''' Push za minimalna kopica '''
    T.append
    i = len(T)-1
    oce = i // 2
    while T[oce] > T[i]:
        T[oce], T[i] = T[i],T[oce]
        i = oce
        oce = i // 2
```

```python
def pop(T): #odstranimo koren
'''Pop za minimalno kopico'''
    koren = T[1]
    T[1] = T[-1]
    T.pop()
    levi_sin = 2 * i
    desni_sin = 2 * i + 1
    while T[i] > T[levi_sin] or T[i] > T[desni_sin]:
        
        if T[levi_sin] > T[desni_sin]:
            T[desni_sin], T[i] = T[i], T[desni_sin]
            i = desni_sin
            levi_sin = 2 * i
            densi_sin = 2 * i + 1

        else:
            T[levi_sin], T[i] = T[i], T[levi_sin]
            i = levi_sin
            levi_sin = 2 * i
            desni_sin = 2 * i + 1

    return koren
```


### **3. naloga**
Kako bi s kopico sortiral seznam? Časovna zahtevnost? Kako in podanega seznama nardiš kopico v O(n) časa.

Da spravimo seznam v kopico potrebujemo $O(n \cdot logn)$ časa. Da pa iz kopice nazaj preberemo elemente pa potrebujemo $O(logn)$ časa. Iz tega sledi da je skupna časovna zahtevnost $O(n \cdot logn)$.


