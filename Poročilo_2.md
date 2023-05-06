# Drugo poročilo za vaje
**Ime:** Alen Nemanič

## Vsebina
- Vaje 5 (15.3.2023)
- Vaje 6 (22.2.2023)
- Vaje 7 (29.3.2023)
- Vaje 8 (5.4.2023)
- Vaje 9 (12.4.2023)
- Vaje 10 (9.4.2023)

## Vaje 5
**Datum**: 15.3.2023

$G = (V, E); V = \{1, \ldots, n\},\ E \subseteq \binom{V}{2}$

### Naloga 1

Predstavitev grafa:

<ol>
<li>Matrika sosednjosti</li>

$A$ je $n \times n$ matrika

$A[i][j] = \begin{cases} w(i, j);\ (i, j) \in E\\ None;\ sicer\end {cases}$

<li>Seznam sosednjosti</li>

$G$ je seznam seznamov dolžine $n$. $G[i] = [(i, w(i, j))$ za vsak $j$, da je $(i, j)$ povezava $]$ 

<li>Slovar sosednjosti</li>

$G$ je seznam slovarjev dolžine $n$

$G[i] = \{j: w(i, j)$ za vsak $j$, da je $(i, j)$ povezava $\}$

</ol>

| Predstavitev grafa | Prostorska zahtevnost | Ali sta $i$ in $j$ sta soseda? | Sosedi od $i$ |
| :-: | :-: | :-: | :-: |
| Matrika sosednjosti | $O(n^2)$ | $O(1)$ | $O(n)$ |
| Seznam sosednjosti | $O(n + m)$ | $O(n)$ | $O(1)$ |
| Slovar sosednjosti | $O(n + m)$ | $O(1)$ | $\begin{cases} O(n);\ če\ želimo\ seznam\ sosedov\\ O(1);\ če\  žeilmo\ množico\ sosedov  \end{cases}$ |

Lema o rokovanju - $\sum_{i=1}^{n} deg(i) = 2 \cdot |E|$

### Naloga 2

Usmerjenemu grafu $G$ z $n$ vozlišči, ki nima ciklov rečemu tudi $DAG$ (directed acyclic graph). Vozlišča takega grafa lahko topološko uredimo. To pomeni, da obstaja da zaporedje vozlišč $(v_1, v_2, \ldots, v_n)$, tako da ne obstaja povezava od $v_i$ do $v_j$, če je $j<i$.

Sestavi algoritem, ki najde tako zaporedje. Namig: Katera vozlišča lahko zagotovo damo na prvo mesto v to ureditev? 

```python
n = len(G)
in_deg = [0] * n # Seznam n ničel
for i in range(n):
    for j in G[i]: # O(n + m), koliko je število vozlišč in povezav
        in_deg[j] += 1
izvori = [i for in in range(n) if in_deg[i] == 0]
rezulat = []
while izvori: # O(n + m)
    izvor = izvori.pop()
    rezultat.append(izvor)
    for sosed in G[izvor]:
        in_deg[sosed] -= 1
        if in_deg[sosed] == 0:
            izvori.append(sosed)
return rezultat
```

### Naloga 3
Naj bo sedaj $G$ usmerjen utežen graf brez ciklov. Kako bi izračunal ceno najdaljše poti v tem grafu med vozliščema $s$ in $t$.

$D(i)\ -$ najdaljša pot od $i$ do $t$

$D(t) = 0$

$D(i) = \max\{D(j) + w\}$

Graf uredimo topološko in seznam $D$ polnimo v obratni topološki ureditvi.

## Vaje 6
**Datum**: 15.3.2023

### Naloga 1

Ponovili smo *BFS Algoritem* (Iskanje v širino).

Z BFS lahko najdemo najkrajšo pot od poljubnega vozlišča do katerega koli drugega vozlišča.

BFS lahko uporabimo za:
- Pregled grafa
- Vpeto drevo/gozd v grafu, povezane komponente
- Preverjanje dvodelnosti grafa
- Iskanje najkrajših poti (neuteženi graf)

$G$ - graf kot seznam sosedov

$u$ - začetno vozlišče

```python
from collections import Deque

def BFS(G, u):
    n = len(G)
    obiskani = [False] * n
    q = vrsta([n]) # Začnemo v n
    while g:
        trenutni = g.popleft()
        if obiskani[trenutni]: continue # Smo ga že obiskali
        obiskani[trenutni] = True
        for sosed in G[trenutni]:
            if not obiskani[sosed]:
                g.push(sosed)
```

Ta koda za $BFS$ je narejena z vrsto, če bi pa uporabili sklad bi imeli $DFS$.

Če bi želeli poiskati najkrajšo pot, bi morali kodo modificirati.

```python
def BFS(G, u):
    """Vrne najkrajše poti od u do vseh vozlišč."""
    n = len(G)
    d = [0] * n
    obiskani = [False] * n
    q = vrsta([(u, 0)]) # Začnemo v n
    while g: # Dokler vrsta ni prazna
        trenutni, razdalja = g.popleft()
        if obiskani[trenutni]: continue # Smo ga že obiskali
        obiskani[trenutni] = True
        d[trenutni] = razdalja
        for sosed in G[trenutni]:
            if not obiskani[sosed]:
                g.push((trenutni, razdalja + 1))
    return d
```

Časovna zahtevnost tega programa je $O(n + m)$, kjer $n$ predstavlja število vozlišč, $m$ pa predstavlja število povezav.

### Naloga 2

Ponovi $Floyd-Warshallow$ algoritem. Kaj računa in kaj vrne? Kakšna je njegova časovna zahtevnost.

$Floyd-Warshallov$ algoritem:

Vhod: graf $G$, utežen (dovoljene so negativne uteži)

Izhod: $D$ dimenzije $n \times n$ ($n$ predstavlja število vozlišč)
        $D_{ij}$ cena najkrajše poti med $i$-tim in $j$-tim vozliščem

Ideja: $D_{ij} = \min{\{D_{ij}(k-1), D_{ik}(k-1) + D_{kj}(k-1)\}}$

Robni pogoji: 

$D_{ii}(1) = 0$

$D_{1i}(1) = w_{1i}$, utež te povezave

Časovna zahtevnost je $O(n^3)$, prostorka pa $O(n)$.

### Naloga 3

Simuliraj FW algoritem na spodnjem grafu. 

![image](../Datoteke/Vaje%206/graf.png)

|   | 1 | 2 | 3 | 4 | 5 |
|:-:|:-:|:-:|:-:|:-:|:-:| 
| 1 | 0 | 2 | $\infty$, 3 | 8, 5 | $\infty$, 7 | 
| 2 | $\infty$, 8, 6 | 0 | 1 | $\infty$, 3 | $\infty$, 5 | 
| 3 | $\infty$, 7, 5 | $\infty$, 0 | 0 | 2 | $\infty$, 4 |
| 4 | $\infty$, 5, 3 | -2 | $\infty$, -1 | 0 | 2 |
| 5 | 1 | 7, 3, -3 | -3 | $\infty$, 9, 1 | 0 |  

## Vaje 7
**Datum**: 29.3.2023

### Naloga 1

Iz prejšnjih vaj obravnavaj, kako razberemo najkrajše poti s pomočjo matrike $\Pi$, ki jo dobimo z FW algoritmom.

$F-W: D_{ij}(k) = \min{\{D_{ij}(k-1), D_{ik}(k-1)+D_{kj}(k-1)\}}$

$\Pi_{ij}(k)$ - zadnje vozlišče na i-j poti, kjer moramo vmes uporabljati samo vozlišča od 1 do k

Floyd Warshall: $D_{i,j} = \min{D_{i,j}(k-1), D_{i,k}(k-1) + D_{k,j}(k-1)}$

$\Pi_{i,j}(k) ...$  predstavlja zadnje vozlišče na $i-j$ pot, kjer smemo vmes uporabiti samo vozlišča od 1 do $k$.

Začetni pogoji: $\Pi_{i,i} (0) = i$
- A: $\Pi_{i,j} (k)= \Pi_{i,j}(k-1) \cdot \Pi_{i,G[i]}(0) = i$

- B: $\Pi_{i,j} (k) = \Pi_{k,j}(k-1)$


**Rekonstrukcija poti:**

VHOD: vozlišči $i,j$, matrika $\Pi(n)$

IZHOD: najkrajša pot od $i$ do $j$

ALGORITEM:
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

### Naloga 2

Uteži sedaj dodamo še na vozlišča. Kako sedaj poiskati najcenejše poti?

Možne ideje:

- Prištejemo povezavi, ki kaže v to vozlišče
- Prištejemo povezavi, ki kaže iz vozlišča
Odločimo se glede na problem, smiselno obravnavamo začetno in končno vozlišče.

### Naloga 4

Na neki borzi se trgujejo valute po menjalnem tečaju, ki ga podaja tabela R velikosti $n \times n$, kjer je n število različnih valut. Vrednost $R[i][j]$ pove, da za a enot valute $i$ dobimo $a⋅R[i][j]$ enot valuje $j$. Ker menjalni tečaji lahko hitro spreminjajo in so odvisni od raznih parametrov se lahko zgodi, da $R[i][j]⋅R[j][i]≠1$.

Za primer si oglejmo naslednjo shemo: 

|  | EUR | USD | YEN |
| :-: | :-: | :-: | :-: |
| EUR | 1 | 1.2 |   |
| USD |   | 1 | 120 |
| YEN | 0.01 |   | 1 |

Če trgujemo USD -> YEN -> EUR -> USD končamo z 1.44 USD. Tako zaporedje imenujemo arbitraža.

Predpostavi, da ne obstaja arbitražnih zaporedij. Kako bi poiskal najbolj ugodno pretvorbo valute $i$ v valuto $j$?

Kaj pa če sedaj opustimo predpostavko in dovoljujemo, da arbitražna zaporedja obstajajo. Kako bi odkril, kakšna so?

- Sestavimo graf $G(V, E)$
- Vozlišča so valute, v našem primeru so to EUR, USD, YEN
- Povezave nam predstavljajo pretvorbo valut
Zanima nas "najdražja pot" v grafu od $i$ do $j$

### Naloga 5

Ponovi Djikstrov algoritem. Kaj so vhodni in izhodni podatki, kakšne so predpostavk, itd.

Vhodni podatki:
* Usmerjen graf $G(V,e)$
* začetno vozlišče $s \in V$
* $c_{i,j} \geq 0 $, cene so pozitivne

Izhodni podatki:
* cene najcenejših poti od $s$ do $i$ $\forall i \in V$ --> D
* drevo najkrajših poti od $s$ do $i$ $\forall i \in V$ --> P

```python
def dijkstra(G, s):
    """Vrne najkrajšo pot od s do vseh vozlišč v grafu G"""
    n = len(G)
    D = [float("inf")] * n
    P = [None] * n
    D[s] = 0 # D[i] pove razdaljo od s do i. Pri nas je i = s
    P[s] = s
    obiskani = [False] * n
    q = Vrsta(V(G))  # V vrsto dodamo še nedodana vozlišča
    while len(obiskani) != n:
        c = q.popmin()  # Dobimo najmnajši element in ga odstrani iz seznama
        obiskani.add(c)
        for sosed, utez in G[c]:
            if sosed not in obiskani:
                if D[c] + utez + D[sosed]:
                    D[sosed] = D[c] + utez
                    P[sosed] = c
    return D,P
```

pri tem nam
```python
c.popmin()
```
pove, da pogledamo vsa vozlišča v q in vrnemo tistega z najnižjim $D[\ ]$

## Vaje 8
**Datum**: 5.4.2023

Na [naslovu](https://unilj-my.sharepoint.com/:f:/g/personal/gasper_romih_fmf_uni-lj_si/EgIVtB_YcP1Cs6MMyjtiFCcBSEEHYH9rzpd63Ll_sXAXrA?e=QMRZzr) imate na razpolago dve datoteki:

- djikstra.py -> moja implementacija djikstrovega algoritma
- roadNet-TX.txt -> datoteka za informacijami o cestnem omrežju v Texasu. Vozlišča so bodisi križišča oz. končne destinacije povezave pa so ceste med temi vozlišči. Povezave oz. ceste niso utežene so pa usmerjene.

### Naloga 1

Vaša naloga bo, da uporabite ta algoritem na teh podatkih, torej:

- roadNet-TX.txt spremenite v ustrezno podatkovno strukturo grafa.

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

- poiščete najkrajše razdalje od vozlišča $100$ do vseh ostalih.

```˙python
print(razdalje[100000])
```

- Koliko je razdalja $d_G(100, 100000)$?

```˙python
razdalje, poti = djikstra(G, 100)
```

- Katero vozlišče je najbolj oddaljeno od vozlišča $100$?

```˙python
print(len(graf[100]))
```

- Koliko vozlišč je dosegljivih iz vozlišča $100$?

```˙python
print(len(graf[100]))
```

### Naloga 2

Glede na to, da graf ni utežen, lahko za isto nalogo implementiramo $BFS$ algoritem. Implementiraj $BFS$ algoritem, ki bo poiskal dolžine najkrajših poti od $s$ do vseh ostalih vozlišč. Vrne naj tudi drevo najkrajših poti, tako kot $Djikstra$. Preveri iste zadeve kot zgoraj, dobiti moraš seveda iste odgovore.

```python
def bfs_iskanje(G, u):
    n = len(G)
    d = [0] * n
    obiskani = [False] * n
    q = [(u, 0, u)]
    poti = [None] * n
    while q:
        trenutni, razdalja, pred = q.pop(0)
        if obiskani[trenutni]:
            continue
        obiskani[trenutni] = True
        d[trenutni] = razdalja
        poti[trenutni] = pred
        for sosed, cena in G[trenutni]:
            if not obiskani[sosed]:
                q.append((sosed, razdalja + 1, trenutni))
    return d, poti
```

### Naloga 3

Oba algoritma dodelaj, tako da dodaš nov vhodni podatek $t$, ki predstavlja končno vozlišče. Algoritma naj torej vrneta razdaljo med $s$ in $t$ v grafu, ter poti (kot drevo) med njima. Delujeta naj, tako da se ustavita takoj ko najdemo željeno pot.

```python
def BFS_dodelan(G, u, t):
    '''Funkcija vrne seznam poti od vozlisca u do vozlišča t v grafu G'''
    n = len(G)
    razdalje = [0] * n
    obiskani = [False] * n
    q = ([(u,0,u)])
    poti =[None] * n
    while q:
        trenutni, razdalja, prejsni = q.pop(0)
        if obiskani[trenutni]:
            continue
        if trenutni == t:
            break
        obiskani[trenutni] = True
        razdalje[trenutni] = razdalja
        poti[trenutni] = prejsni
        for sosed, teza in G[trenutni]:
            if not obiskani[sosed]:
                q.append((sosed, razdalja + 1, trenutni))
    return razdalje, poti
```

### Naloga 4

Zapiši funkcijo, ki sprejme začetno vozlišče $s$, končno vozlišče $t$ in drevo najkrajših poti, ter vrne najkrajšo pot med njima v obliki seznama.

Sedaj rekonstruiraj najkrajšo pot med vozliščem $100$ in $100000$.

```python
def pot_s_t(s, t, drevo_najkrajsih):
    sez = list()
    v = drevo_najkrajsih[t]
    sez.append(t)
    while v != s:
        sez.append(v)
        v = drevo_najkrajsih[v]
    sez.append(s)
    return sez
```

## Vaje 9
**Datum**: 12.4.2023

### Naloga 2

Konstruirajte nov graf, ki vsebuje le vozlišča od $0$ do $n$.

Vsaki povezavi določite neko pozitivno utež (lahko čisto naključno) in zadevo shranite v novo .txt datoteko. Vrstice naj bodo oblike $u$ v $w(u,v)$, kjer je $(u,v)$ povezava in $w(u,v)$ njena utež.

```python
import random

def generiraj_graf(n):
    graf=list()
    for vozlisce in range(n+1):
        tab = list()
        for sosed in range(random.randint(1,n+1)):
            tab.append((random.randint(0,n), random.randint(1,10)))
        graf.append(tab)
    return graf


def zapisi_txt(ime, graf):
    with open(ime + '.txt', 'w') as dat:
        for ind, sosedje in enumerate(graf):
            for sosed in sosedje:
                vrstica = '{} {} {}\n'
                dat.write(vrstica.format(ind, sosed[0], sosed[1]))


g1 = generiraj_graf(49)
zapisi_txt('graf_g1', g1)
```

### Naloga 3

Implementiranje še $Bellman-Fordov$ algoritem in ga poženite na grafu iz prejšnje naloge. Analiziraje kako velik $n$ iz prejšne naloge morate vzeti, da bo algoritem še deloval v zglednem času.

```python
def Bellman_Ford(graf, zacetek, n):
    razdalje = [float('Inf')]*n
    razdalje[zacetek] = 0
    
    for korak in range(n-1):
            if razdalje[u] + w < razdalje[v]:
                razdalje[v] = razdalje[u] + w
    for u, v, w in graf:
        if razdalje[u] != float('Inf') and razdalje[u] + w < razdalje[v]:
            return None
    return razdalje

def seznam_povezav_BF(ime_dat):
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

## Vaje 10
**Datum**: 19.4.2023

Kopica je levoporavnano dvojiško drevo

Lastnost kopice:
- Oče je manjši ali enak sinoma (Minimalna kopica)
- Oče je večji ali enak sinoma (Maksimalna kopica)

### Naloga 1

Simuliraj delovanje minimalne kopice. Za vsavljanje je kot operacija število, za brisanje pa x. Za boljšo predstavo nariši kar drevesa.

Operacije: 8,2,1,3,7,6, x, x, 5, x, -3, x

![](vaje_10_kopica.png)


### Naloga 2 

Predstavi kopico s seznamom in zapiši delovanje pop() in push(x) operacij.

T je seznam dolžine $n$ (kopica)

T[$i$] - vozlišče

Sinovi od $i$ so $2i$ in $2i+1$, če je prvi indeks v tabeli enak 1, če je prvi indeks v tabeli enak 0, sta sinova $2i+1$ in $2i+2$.

Oče je v primeru, da je prvi indeks v tabeli enak 0, na indeksu  $(i-1) // 2$

```python
def push(T,x):
    """Push za minimalno kopico"""
    T.append
    i = len(T) - 1
    oce = i // 2
    while T[oce] > T[i]:
        T[oce], T[i] = T[i],T[oce]
        i = oce
        oce = i // 2
```

```python
def pop(T): #odstranimo koren
    """Pop za minimalno kopico"""
    koren = T[1]
    T[1] = T[-1]
    T.pop()
    levi_sin = 2 * i
    desni_sin = 2 * i + 1
    while T[i] > T[levi_sin] or T[i] > T[desni_sin]:
        if T[levi_sin] > T[desni_sin]:
            T[desni_sin], T[i] = T[i], T[desni_sin]
            i = desni_sin
        else:
            T[levi_sin], T[i] = T[i], T[levi_sin]
            i = levi_sin
        levi_sin = 2 * i
        desni_sin = 2 * i + 1
    return koren
```

### Naloga 3
Kako bi s kopico sortiral seznam? Časovna zahtevnost? Kako iz podanega seznama narediš kopico v O(n) časa.

Heap sort ne more delati hitreje kot $O(n \cdot logn)$

"Heapify" - Iz seznama želimo narediti kopico.

Seznam tretiramo kot kopico:
- Levoporavnano dvojiško drevo (izpolnjeno)
- Lastnosti kopice (ni izpolnjeno)

Časovna zahtevnost:
<ol>
<li> Shift up </li>

$\sum_{i=0}^{log(n)} 2^i \cdot i = \sum_{i=0}^{n-1}i \cdot log(i) = O(n\cdot logn)$

<li> Shift down </li>

$\sum_{i=1}^{logn} \frac{n}{2^i} \cdot (i-1) = \sum_{i=0}^{logn} \frac{n}{2^{i+1}} \cdot (i-1) \leq \frac{n}{2} \sum_{i=1}^{\infty} i \cdot 2^{-i}$
</ol>