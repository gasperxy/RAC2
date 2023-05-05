<h1 align="center"> Vaje 5 </h1>

## Datum: 15.3.

___
___

## Naloga 1

### Imamo graf usmerjen `G=(V,E)` z uteženimi povezavami. Torej imamo neko funkcijo $\omega :E \to A$, ki vsaki povezavi dodeli utež iz množice $A$.

### Navedi nekaj možnih podatkovnih struktur za predstavitev grafa `G`. Navedi nekaj prednosti oz. slabosti vsake izmed njih. Ponovi tudi, kaj je v grafu pot, sprehod in cikel.


Predstavitev grafa:

- matrika sosednosti
- seznam sosednosti $G$
- slovar sosednosti $G$

### <ins>Matrika sosednosti</ins>
$$
A[i][j] = \left \\{ \begin{array}{ll}
\omega(i,j) & , (i,j) \in E \\ 
\text{None} &\text{, sicer}
\end{array} 
\right.
$$

<br>

### <ins>Seznam sosednosti</ins> $G$

$G$ je seznam seznamov dolžine $n$. <br>
$G[i]=[(j,\omega (i,j));\ \forall j, \ da \ (i,j)\in E ]$ 

<br>

### <ins>Slovar sosednosti</ins> $G$

$G$ je seznam slovarjev dolžine $n$ <br>
$G[i]= \{j:\omega(i,j);\ \forall j, \ da \ (i,j) \in E \}$



||prostorska zahtevnost|$i$ in $j$ soseda?|sosedi od $i$|
|:--:|:--:|:--:|:--:|
matrika sosednosti|$O(n^2)$|$O(1)$|$O(n)$|
seznam sosednosti|$O(m+n)$|$O(n)$|$O(1)$|
slovar sosednosti|$O(m+n)$|$O(1)$|$O(n)$/$O(1)$

___

## Naloga 2

### Usmerjenemu grafu $G$ z $n$ vozlišči, ki nima ciklov rečemu tudi DAG (directed acyclic graph). Vozlišča takega grafa lahko topološko uredimo. To pomeni, da obstaja da zaporedje vozlišč $(v_1,v_2,\dots , v_n)$, tako da ne obstaja povezava od $v_i$ do $v_j$, če je $j < i$.

<br>

### Primer grafa:

<img src=graf1.png  width="60%" height="60%"> 

### DAG ureditev:

<img src=graf2.png  width="60%" height="60%"> 

### Algoritem, ki najde tako zaporedje.

<img src=koda.png  width="60%" height="60%"> 

Z rdečo je zapisana časovna zahtevnost posameznega dela.

___

## Naloga 3

### _Naj bo sedaj $G$ usmerjen utežen graf brez ciklov. Kako bi izračunal ceno najdaljše poti v tem grafu med vozliščema $s$ in $t$._

$D[i]$ = najdaljša pot od $i$ do $t$ \
$D[t]=0$, $D[i] = - \infty$ \
$D[j]=\max\limits_{(i,j)\in G[i]}(D[j]+\omega)$

Graf uredimo topološko in seznam D polnimo v obratni topološki ureditvi.

___
___

<h1 align="center"> Vaje 6 </h1>

## Datum 22.3.
___
___

## Naloga 1
### _Ponovi BFS algoritem. Modificiraj ga, tako da bo iskal najkrajše poti v neuteženem grafu._
### BFS - "Breadth-first search"

<img src=bfs.png  width="60%" height="60%">

Uporablja se za:
- pregled grafa
- vpeto drevo/gozd v grafu, povezane komponente
- preverjanje dvodelnosti grafa
- iskanje najkrajše poti (neutežen graf)

``` python
def bfs(G,u):
    n = len(G)
    obiskani = [False]*n
    q = vrsta([u]) #začnemo v u
    while q:
        trenutni = q.popleft()
        if obiskani[trenutni]: continue
        obiskani[trenutni] = True
        from sosed in G[trenutni]:
            if not obiskani[sosed]:
                q.push(sosed)
```
Za iskanje poti:

``` python
def bfs_iskanje(G,u):
    '''vrne najkrajše poti od u do vseh vozlisc'''
    n = len(G)
    d = [0]*n
    obiskani = [False]*n
    q = vrsta([(u,0)]) #začnemo v u
    while q:
        trenutni,razdalja = q.popleft()
        if obiskani[trenutni]: continue
        obiskani[trenutni] = True
        d[trenutni] = razdalja
        from sosed in G[trenutni]:
            if not obiskani[sosed]:
                q.push((sosed,razdalja+1))
    return d
``` 

Časovna zahtevnost:
- $O(n+m)$
- $n \dots št. \ vozlišč$
- $m \dots št. \ povezav$

___

## Naloga 2

### Floyd-Warshallow algoritem

Vhod: 
- graf `G` utežen (dovoljene tudi negativne uteži)

Izhod: 
- $D$ dimenzije $n \times n$, ($n \dots št. \ vozlišč$)
- $D_{ij} \dots$ cena najdaljše poti med $i$-tim in $j$-tim vozliščem

Ideja:
- $D_{ij}^{(k)} = min(D_{ij}^{(k-1)}, \ D_{ik}^{(k-1)}+D_{kj}^{(k-1)})$
- $D_{ij}^{(k)} \dots$ isto kot $D_{ij}$ le da uporabljamo vozlišča od $1$ do $k$

Robni pogoji:
- $D_{ii}^{(1)} = 0$
- $D_{1i}^{(1)}= \omega_{1i}$ (utež povezave)

Časovna zahtevnost $O(n^3)$:
- $n$ matrik
- matrike so velikosti $n \times n$

Prostorska zahtevnost: $O(n^2)$

___
## Naloga 3

<img src=povezave.png  width="60%" height="60%">


||1|2|3|4|5|
|:--:|:--:|:--:|:--:|:--:|:--:|
|1|$0$|$2$|$\infty,3_2$|$8,5_3$|$\infty,7_4$|
|2|$\infty,8_4,6_5$|$0$|$1$|$\infty,3_3$|$\infty,5_4$|
|3|$\infty,7_4,5_5$|$\infty$|$0$|$2$|$\infty,4_4$|
|4|$\infty,5_3,3_5$|$-2$|$\infty,-1_2$|$0$|$2$|
|5|$1$|$7,3_1,-3_4$|$-3$|$\infty,9_1,-1_3$|$0$|

___
___
<h1 align="center"> Vaje 7 </h1>

## Datum 29.3.
___
___
## Naloga 1

### Iz prejšnjih vaj obravnavaj, kako razberemo najkrajše poti s pomočjo matrike $\Pi$, ki jo dobimo z FW algoritmom.

<br>

F-W: $D_{ij}^{k} = min({\color{green}D_{ij}^{k-1}}, \ {\color{red} D_{ik}^{k-1}+D_{kj}^{k-1}})$

$\Pi_{ij}^{k} \ \dots$ zadnje vozlišče na i-j poti, kjer smemo uporabiti vozlišča od 1 do k

### Začetni/robni pogoji:
$\large\Pi_{ii}^{0} = i$ \
$\large\Pi_{iG[i]}^{0} = i$ \
${\color{green}\large\Pi_{ij}^{k} = \Pi_{ij}^{k-1}}$ \
${\color{red}\large\Pi_{ij}^{k} = \Pi_{kj}^{k-1}}$

<br>

### Rekonstrukcija poti
Vhod: vozlišče $i,j$, matrika $\Pi^{n}$ \
Izhod: najkrajša pot od $i$ do $j$

Algoritem:
``` python
def rekonctrukcija(i,j,Pi):
    p = j
    pot = []
    while p != i:
        pot.append(p)
        p = Pi[i][p]
    pot.append(i)
    return pot.reverse()
```
ČZ: $O(n)$
___

## Naloga 2

### Uteži sedaj dodamo še na vozlišča. Kako sedaj poiskati najcenejše poti?

<br>

Možne ideje:
1. Prištejemo povezavi, ki kaže v to vozlišče
2. Prištejemo povezavi, ki kaže iz vozlišča

Odločimo se glede na problem, smiselno obravnavamo začetno in končno vozlišče.

___

## Naloga 3

### Premisli, zakaj preprosta sprememba v FW algoritmu iz min na max ne najde nujno najdražje poti v grafu.

<br>

<img src=poti.png  width="40%" height="40%">

Možne poti iz tocke $1$ do tocke $3$:
- $1 \rightarrow 3$
- ${\color{red}1 \rightarrow 2 \rightarrow 3}$

Možne poti od $1$ do $2$:
- $1 \rightarrow 2$
- ${\color{red}1 \rightarrow 3 \rightarrow 2}$

Možne poti od $2$ do $3$:
- $2 \rightarrow 3$
- ${\color{red}2 \rightarrow 1\rightarrow 3}$

Ker iščemo maksimalno razdaljo izberemo rdeče povezave (možnosti). \
Vendar ti dve poti nista "kompatibilne", to pomeni če te poti združimo se ponavljajo vozlišča in povezave.

Ideja je narediti inverz grafa tako da so negativne vrednosti. Vendar pa to deluje le v grafih, ki nimajo pozitivnih ciklov.

___
## Naloga 4

### <ins>Navodila</ins>:
Na neki borzi se trgujejo valute po menjalnem tečaju, ki ga podaja tabela R velikosti n×n, kjer je n število različnih valut. Vrednost $R[i][j]$ pove, da za a enot valute i dobimo $a\cdot R[i][j]$ enot valuje j. Ker menjalni tečaji lahko hitro spreminjajo in so odvisni od raznih parametrov se lahko zgodi, da $R[i][j]\cdot R[j][i] \neq 1$.

<br>

<img src=primer.png  width="60%" height="60%">

<br>

Če trgujemo USD -> YEN -> EUR -> USD končamo z 1.44 USD. Tako zaporedje imenujemo arbitraža.

Predpostavi, da ne obstaja arbitražnih zaporedij. Kako bi poiskal najbolj ugodno pretvorbo valute $i$ v valuto $j$?

<br>

### <ins>Rešitev</ins>:

Sestavimo graf $G(E,V)$ \
Vozlišča - valute \
Povezave - pretvorba

Zanima nas "najdražja pot" v zgornjem grafu $i-j$. Ceno poti dobimo kot produkt uteži na povezavah.

Da pretvorimo produkt v vsoto uporabimo logaritem oz. logaritemsko funkcijo. Na povezave damo $\log(R_{i_1,i_2})$, kjer je $R_{i_1,i_2}$ prevorba iz $i_1$ v $i_2$ valuto. 
\
Uporaba logaritemske funkcije:
$\log(a \cdot b) = \log(a) \cdot \log(b)$
\
Utež na povezavi $i$-$j$ nastavimo na $-\log(R_{i,j})$
\
V ta namen želimo uporabiti F-W algoritem (to lahko naredimo če graf nima negativnih ciklov)

<br>

### Pokažimo da jih naš graf res nima:
Dokažemo s protislovjem: \
Predpostavimo da imamo negativen cikel od $i$-$i$

cena cikla: <br>
$- \sum \limits_{j=1}^{k} \log(R(i_{j-1},i_{j})) < 0$ \
$\log(\prod \limits_{j=1}^{k}R(i_{j-1},i_{j}) > 0$ \
$\prod \limits_{j=1}^{k}R(i_{j-1},i_{j}) > 1$ \
To je protislovje $\rightarrow \leftarrow$

___
## Naloga 5

Vhodni podatki: 

&nbsp;&nbsp; $G(V,E)$ \
&nbsp;&nbsp; začetno vozlišče \
&nbsp;&nbsp; $C_{i,j} \ \geq 0$, uteži so pozitivne

<br>

Izhodni podatki: 

&nbsp;&nbsp; cene najcenejših poti: $s \rightarrow i$, $\forall i \in V \ \ \ \ \thicksim D$\
&nbsp;&nbsp; drevo najkrajšh poti od $s$ do $i$, $\forall i \in V \ \ \ \ \thicksim P$

``` python
def dijkstra(G,s):
    n = len(G)
    D = [inf]*n
    P = [None]*n
    D[s] = 0
    P[s] = s
    obiskani = set()
    q = vrsta(V(G))
    while len(obiskani) != n:
        c = q.popmin()
        obiskani.add(c)
        for sosed, utež in G[c]:
            if sosed not in obiskani:
                if D[c] + utež < D[sosed]:
                    D[sosed] = D[c] + utež
                    P[sosed] = c
    return D,P
``` 

ČZ: $O(n^2)$

___
___

<h1 align="center"> Vaje 8 </h1>

## Datum 5.4.
___
___
## Naloga 1
### Implementacija djikstrovega algoritma
``` python
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

### roadNet-TX.txt spremenjena v ustrezno podatkovno strukturo grafa

```python
def naj():
    naj = 0
    with open('roadNet-TX.txt','r') as f:
            vrstice =f.readlines()
            veljavne = vrstice[4:]
            for vrstica in veljavne:
                trenutna = vrstica.strip().split("\t")
                od = int(trenutna[0])
                do = int(trenutna[1])
                if od > naj:
                    naj = od
    return naj
            
def omrezje(n):
    vse = [[] for _ in range(n+1)]
    with open('roadNet-TX.txt','r') as f:
        vrstice =f.readlines()
        veljavne = vrstice[4:]
        for vrstica in veljavne:
            trenutna = vrstica.strip().split("\t")
            od = int(trenutna[0])
            do = int(trenutna[1])
            vse[od].append((do,1))
    return vse

seznam = omrezje(naj())
``` 
### Poiščete najkrajše razdalje od vozlišča 100 do vseh ostalih
```python
razdalje, poti = djikstra(seznam, 100)
print(f"Najkrajše razdalje od vozlišča 100 do vseh ostalih: \n{poti}\n")
``` 

### Koliko je razdalja d<sub>G</sub>(100,100000)

```python
print(f"Razdalja od 100 do 100000: \n{razdalje[100000]}\n")
# Odgovor: 240
``` 
### Katero vozlišče je najbolj oddaljeno od vozlišča 100?

```python
print(f"Najbolj oddaljeno vozlišče od vozlišča 100: {naj}\n")
# Ogdovor: 1389039
``` 

### Koliko vozlišč je dosegljivih iz vozlišča 100?
```python
koliko = sum([1 for el in razdalje if el > 0])
print(f"{koliko} vozlišč je dosegljivih iz vozlišča 100\n")
# Odgovor: 1351136
``` 
___
## Naloga 2

### Glede na to, da graf ni utežen, lahko za isto nalogo implementiramo BFS algoritem. Implementiraj BFS algoritem, ki bo poiskal dolžine najkrajših poti od s do vseh ostalih vozlišč. Vrne naj tudi drevo najkrajših poti, tako kot Djikstra. Preveri iste zadeve kot zgoraj, dobiti moraš seveda iste odgovore.

```python 
def bfs_iskanje2(G, u):
    '''vrne najkrajše poti od u do vseh vozlisc'''
    n = len(G)
    d = [0]*n
    obiskani = [False]*n
    q = [(u, 0, u)]  # začnemo v u
    poti = [None]*n
    while q:
        trenutni, razdalja, pred = q.pop(0)
        if obiskani[trenutni]:
            continue
        obiskani[trenutni] = True
        d[trenutni] = razdalja
        poti[trenutni] = pred
        for sosed, cena in G[trenutni]:
            if not obiskani[sosed]:
                q.append((sosed, razdalja+1, trenutni))
    return d, poti


razdalje2, poti2 = bfs_iskanje2(seznam, 100)

print(f"Najkrajše razdalje od vozlišča 100 do vseh ostalih: \n{poti2}\n")

print(f"Razdalja od 100 do 100000: \n{razdalje2[100000]}\n")
# Odgovor: 240

naj2 = razdalje2.index(max(razdalje2))
print(f"Najbolj oddaljeno vozlišče od vozlišča 100: {naj2}\n")
# Odgovor: 1389039

koliko2 = sum([1 for el in razdalje2 if el > 0])
print(f"{koliko2} vozlišč je dosegljivih iz vozlišča 100")
# Odgovor: 1351136
``` 
___

## Naloga 3

### Oba algoritma dodelaj, tako da dodaš nov vhodni podatek t, ki predstavlja končno vozlišče. Algoritma naj torej vrneta razdaljo med s in t v grafu ter poti (kot drevo) med njima. Delujeta naj, tako da se ustavita takoj ko najdemo željeno pot.

```python 
import heapq
from collections import deque


def djikstra_koncna(G, s, t):
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

        if u == t:
            break

        # gremo čez vse sosede in dodamo potrebne elemente na vrsto.
        for (v, teza) in G[u]:
            if not obiskani[v]:

                # heap.heappush(Q, elem) doda element v seznam Q, kjer ohranja lastnost kopice.
                heapq.heappush(Q, (razdalja + teza, v, u))

    return razdaljeDo, poti


def bfs_iskanje_koncna(G, u, t):
    '''vrne najkrajše poti od u do vseh vozlisc'''
    n = len(G)
    d = [0]*n
    obiskani = [False]*n
    q = [(u, 0, u)]  # začnemo v u
    poti = [None] * n
    while q:
        trenutni, razdalja, prej = q.pop(0)
        if obiskani[trenutni]:
            continue
        obiskani[trenutni] = True
        d[trenutni] = razdalja
        poti[trenutni] = prej

        if trenutni == t:
            break

        for sosed, cena in G[trenutni]:
            if not obiskani[sosed]:
                q.append((sosed, razdalja+1, trenutni))
    return d, poti

``` 
___

## Naloga 4

### Zapiši funkcijo, ki sprejme začetno vozlišče s, končno vozlišče t ter drevo najkrajših poti ter vrne najkrajšo pot med njima v obliki seznama. <br> Sedaj rekonstruiraj najkrajšo pot med vozliščem 100 in 100000.

```python
def pot(s, t, drevo):
    rez = []
    while t != s:
        rez.append(t)
        t = drevo[t]
    rez.append(s)
    return rez

print(pot(100, 100000, djikstra_koncna(omrezje(naj()), 100, 100000)[1]))
``` 
____

## Naloga 5

### Analiziraj časovne zahtevnosti algoritmov. Primerjaj hitrost med djikstro in BFS-jem. Prav tako analiziraj razliko med djikstro, ki izračuna najkrajše poti od s do vseh ostalih ter jo primerjaj z tisto verzijo iz Naloge 3.

```python
import matplotlib.pyplot as plt
import time
from djikstra import djikstra
from BFS import bfs_iskanje2
from fun_naloga3 import djikstra_koncna, bfs_iskanje_koncna


def naj():
    naj = 0
    with open('roadNet-TX.txt', 'r') as f:
        vrstice = f.readlines()
        veljavne = vrstice[4:]
        for vrstica in veljavne:
            trenutna = vrstica.strip().split("\t")
            od = int(trenutna[0])
            do = int(trenutna[1])
            if od > naj:
                naj = od
    return naj


def omrezje(n):
    vse = [[] for _ in range(n+1)]
    with open('roadNet-TX.txt', 'r') as f:
        vrstice = f.readlines()
        veljavne = vrstice[4:]
        for vrstica in veljavne:
            trenutna = vrstica.strip().split("\t")
            od = int(trenutna[0])
            do = int(trenutna[1])
            vse[od].append((do, 1))
    return vse


rez = omrezje(naj())


x4 = []
y4 = []

for i in [100, 1000, 10000, 100000, 1000000]:
    skupaj = 0
    for _ in range(6):
        zacetek = time.time()
        bfs_iskanje_koncna(rez, 100, i)
        konec = time.time()
        skupaj += konec-zacetek
    x4.append(i)
    y4.append(skupaj/6)


x3 = []
y3 = []

for i in [100, 1000, 100000, 1000000]:
    skupaj = 0
    for _ in range(6):
        zacetek = time.time()
        bfs_iskanje2(rez, 100)
        konec = time.time()
        skupaj += konec-zacetek
    x3.append(i)
    y3.append(skupaj/6)


x2 = []
y2 = []

for i in [100, 1000, 10000, 100000, 1000000]:
    skupaj = 0
    for _ in range(6):
        zacetek = time.time()
        djikstra_koncna(rez, 100, i)
        konec = time.time()
        skupaj += konec-zacetek
    x2.append(i)
    y2.append(skupaj/6)

x1 = []
y1 = []

for i in [100, 1000, 100000, 1000000]:
    skupaj = 0
    for _ in range(6):
        zacetek = time.time()
        djikstra(rez, 100)
        konec = time.time()
        skupaj += konec-zacetek
    x1.append(i)
    y1.append(skupaj/6)

plt.plot(x1, y1, label="djikstra samo začetek")
plt.plot(x2, y2, label="djikstra začetek in konec")
plt.plot(x3, y3, label="bfs samo začetek")
plt.plot(x4, y4, label="bfs začetek in konec")
plt.title("Časovna zahtevnost")
plt.legend()
# plt.savefig("cas_zahtevnost.pdf")
plt.show()
``` 
<img src=cas_zah.png  width="100%" height="100%"> 

<br>

### Če nas bi zanimale najkrajše poti od s do t_1, t_2, ..., t_k, kateri algoritem bi uporabil? Probaj odgovor podat na podlagi parametra k, ter analize, ki si jo opravil.
\
Odg: Uporabil bi BFS, saj je v obeh primerih (končno vozlišče in brez) potreboval manj časa.

ČZ djikstra: $O(V + E \cdot log(V))$\
ČZ BFS: $O(V+E)$

___
___

<h1 align="center"> Vaje 9 </h1>

## Datum 12.4.
___
___

## Naloga 2

### Konstruirajte nov graf, ki vsebuje le vozlišča od 0 do N.
### Vsaki povezavi določite neko pozitivno utež (lahko čisto naključno) in zadevo shranite v novo .txt datoteko. Vrstice naj bodo oblike u v w(u,v), kjer je (u,v) povezava in w(u,v) njena utež.

<br>
Čisto novi graf:

```python
n = 300

with open("nov_graf.txt", "w") as f:
    ze = []
    for _ in range(7*n):
        od = random.randint(0, n)
        do = random.randint(0, n)
        while do == od:
            do = random.randint(0, n)
        utez = random.randint(2, 10)
        if (od, do) not in ze:
            print(f"{od} {do} {utez}", file=f)
            ze.append((od, do))
    # print(len(ze))


def omrezje_novo(n):
    vse = [[] for _ in range(n+1)]
    with open('nov_graf.txt', 'r') as f:
        vrstice = f.readlines()
        veljavne = vrstice
        for vrstica in veljavne:
            trenutna = vrstica.strip().split()
            od = int(trenutna[0])
            do = int(trenutna[1])
            teza = int(trenutna[2])
            vse[od].append((do, teza))
    return vse

rez = omrezje_novo(n)
```

Nekoliko spremenjen graf iz prejšnjih vaj:

```python
def omrezje(n):
    vse = [[] for _ in range(n+1)]
    with open('roadNet-TX.txt', 'r') as f:
        vrstice = f.readlines()
        veljavne = vrstice[4:]
        for vrstica in veljavne:
            trenutna = vrstica.strip().split("\t")
            od = int(trenutna[0])
            do = int(trenutna[1])
            if do <= n and od <= n:
                vse[od].append((do, 1))
    return vse

rez = omrezje(i)
```

___

## Naloga 3

### Implementiranje še Bellman-Fordov algoritem in ga poženite na grafu iz prejšnje naloge. Analiziraje kako velik N iz prejšne naloge morate vzeti, da bo algoritem še deloval v zglednem času.



```python
def BF(seznam, s):
    n = len(seznam)
    raz = [float("inf")]*n
    prej = [None] * n
    raz[s] = 0

    for _ in range(n):
        for i in range(n):
            for j in range(len(seznam[i])):
                do, utez = seznam[i][j]
                trenutna = raz[i] + utez
                if trenutna < raz[do]:
                    raz[do] = trenutna
                    prej[do] = i

    for i in range(n):
        for j in range(len(seznam[i])):
            do, utez = seznam[i][j]
            if raz[i] + utez < raz[do]:
                print("Neg cikel")
    return raz, prej


def BF_ustavitev(seznam, s):
    n = len(seznam)
    raz = [float("inf")]*n
    prej = [None] * n
    raz[s] = 0
    for _ in range(n):
        sprememba = False
        for i in range(n):
            for j in range(len(seznam[i])):
                do, utez = seznam[i][j]
                trenutna = raz[i] + utez
                if trenutna < raz[do]:
                    sprememba = True
                    raz[do] = trenutna
                    prej[do] = i
        if not sprememba:
            break

    for i in range(n):
        for j in range(len(seznam[i])):
            do, utez = seznam[i][j]
            if raz[i] + utez < raz[do]:
                print("Neg cikel")
    return raz, prej

```

Koda za testiranje velikosti N:

```python
from BF_algoritem import BF, BF_ustavitev
import time
from BFS import bfs_iskanje2
from djikstra import djikstra


def omrezje(n):
    vse = [[] for _ in range(n+1)]
    with open('roadNet-TX.txt', 'r') as f:
        vrstice = f.readlines()
        veljavne = vrstice[4:]
        for vrstica in veljavne:
            trenutna = vrstica.strip().split("\t")
            od = int(trenutna[0])
            do = int(trenutna[1])
            if do <= n and od <= n:
                vse[od].append((do, 1))
    return vse


with open("cas_BF_BFS", "a") as f:
    print(f"{'Število vozlišč':^20} | {'Število povezav':^20} | {'BFS':^20} | {'BF':^20}", file=f)
    print("-"*90, file=f)
for i in range(10000, 300001, 10000):
    rez = omrezje(i)
    z = time.time()
    raz1, pot1 = bfs_iskanje2(rez, 0)
    k = time.time()
    z2 = time.time()
    raz2, pot2 = BF_ustavitev(rez, 0)
    k2 = time.time()
    # z3 = time.time()
    # raz3, pot3 = djikstra(rez, 0)
    # k3 = time.time()
    with open("cas_BF_BFS", "a") as f:
        print(
            f"{f'{i:,}':^20} | {f'{sum([len(el) for el in rez]):,}':^20} | {f'''{k2-z2:.15f} s''':<20} | {f'''{k-z:.15f} s''':<20}", file=f)
```
Izpis zgonje kode:
<img src=cas.png  width="100%" height="100%">

___
___

<h1 align="center"> Vaje 10 </h1>

## Datum 19.4.
___
___ 

## Binarna kopica:
- levo poravnana
- lastnost kopice: $\text{starš} \leq \text{sin} $

___

## Naloga 1

### Simuliraj delovanje (min) kopice. Za vsavljanje je kot operacija število, za brisanje pa x. Za boljšo predstavo nariši kar drevesa.
### Operacije: 8, 2, 1, 3, 7, 6, x, x, 5, x, -3, x

<img src=drevesa1.png  width="100%" height="100%"> \
<img src=drevesa2.png  width="80%" height="80%">

___

## Naloga 2

### Predstavi kopico s seznamom in zapiši delovanje pop() in push(x) operacij.

<br>

$T \ \dots \ seznam \ dolžine \  n \ (kopica)$\
$T[i] \ \dots \ vozlišče$

Sinovi od $i$ so $2i$ in $2i+1$ (če prvi $i=1$), starš $= \lfloor i//2 \rfloor$ \
Sinovi od $i$ so $2i+1$ in $2i+2$ (če prvi $i=0$), starš $= \lfloor (i-1)//2 \rfloor$

<br>
Koda dodaj element:

``` python
def push(T,x):
    '''doda element x v kopico T'''
    T.append(x)
    i = len(T)-1
    oče = i//2
    while T[oče] > T[i]:
        T[oče],T[i]=T[i],T[oče]
        i = oče
        oče = i//2
``` 

Koda odstrani element (ČZ $log(n)$):
``` python
def pop(T):
    '''odstrani prvi element iz kopice'''
    koren = T[1]
    T[1] = T[-1]
    T.pop()
    levi_sin = 2*i
    desni_sin = 2*i+1
    while T[i] > T[levi_sin] or T[i] > T[desni_sin]:
        if T[levi_sin] > T[desni_sin]:
            T[i],T[desni_sin] = T[desni_sin],T[i]
            i = desni_sin
            levi_sin = 2*i
            desni_sin = 2*i+1
        else:
            T[i],T[levi_sin] = T[levi_sin],T[i]
            i = levi_sin
            levi_sin = 2*i
            desni_sin = 2*i+1
    return koren
``` 
___

## Naloga 3

Heap sort ČZ: $\ n\cdot log(n)$ 
<br>

"heapify": iz seznama v kopico \
Seznam tretiramo kot kopico

ČZ: $\sum\limits_{i=0}^{log(n)}2^i \cdot i = \sum\limits_{i=0}^{n-1}i \cdot log(i) = O(n \cdot log(n))$

<img src=heap1.png  width="80%" height="80%">


$\frac{n}{2} \cdot 0 + \frac{n}{4} \cdot 1 +  \frac{n}{8} \cdot 2 + \cdots \leq \sum\limits_{i=1}^{log(n)}\frac{n}{2^i}\cdot (i-1) = \sum\limits_{i=0}^{\lfloor log(n) \rfloor}\frac{n}{2^{i+1}} \cdot i \leq \frac{n}{2} \sum\limits_{i=1}^{\infty} i \cdot 2^{-i} \leq \frac{n}{2} \cdot 2 = n$ 

<img src=heap2.png  width="80%" height="80%">

