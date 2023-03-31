# Primer poročila za vaje
**Ime:** Alen Nemanič

## Vsebina
- Vaje 1 (15.2.2023)
- Vaje 2 (22.2.2023)
- Vaje 3 (1.3.2023)
- Vaje 4 (8.3.2023)

## Vaje 1
**Datum**: 15.2.2023

Na vajah smo ponovili časovne zahtevnosti za seznam, množice in slovarje ter za verižni seznam. Nato smo reševali naloge na Tomo-tu iz dinamičnega programiranja.

### Naloga 1

| Operacija  | Seznam          |Množica / Slovar|  Verižni seznam  |
| :--------: | :-------------: | :------------: |  :------------:  | 
| dodaj(n)   | $O(1)$          | $O(1)$         | $O(1)$ / $O(n)$  |
| dodaj(i)   | $O(n)$          | $O(1)$         | $O(1)$ / $O(n)$  | 
| dodaj(0)   | $O(n)$          | $O(1)$         | $O(1)$ / $O(n)$  | 
| dostop     | $O(1)$          | $O(1)$         | $O(n)$           | 
| $x$ in     | $O(n)$          | $O(1)$         | $O(n)$           | 
| briši(0)   | $O(n)$          | $O(1)$         | $O(1)$ / $O(n)$  | 
| briši(i)   | $O(n)$          | $O(1)$         | $O(1)$ / $O(n)$  | 
| briši(n)   | $O(1)$          | $O(1)$         | $O(1)$ / $O(n)$  |

### Naloga 2

Ukvarjali smo se z problemi iz dinamičnega programiranja.

```python
def zabica_iteracija(mocvara):
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
```

Spodnji graf prikazuje primerjavo med reševanjem problema žabice rekurzivno (zelena) in iteraktivno (rdeča).

![Primerjava problema žabice z rekurzijo in iteraktivno](/Datoteke/Vaje1/graf.png)

## Vaje 2
**Datum**: 22.2.2023

Obravnavali smo problem 0/1 nahrbtnika.

Vhodni podatki so pari $(v_i, c_i)$ za $i = 1, 2, \dots, n$, ki nam povedo velikost in vrednost predmetov

Izhodni podatek je $X = (x_1, x_2, \dots, x_n)$, kjer $x_i = \begin{cases}
1;\ vzamemo\ i-ti\ predmet\\ 0;\ ne\ vzamemo\ i-ti\ predemet
\end{cases}$. 
Veljati mora da je $\sum\limits_{i=1}^{n}v_i \cdot x_i \leq W$, kar nam pove velikost vseh vzetih predmetov, kar pa ne sme presegati. Takrat lahko izračunamo vrednost nahrbtnika $\sum\limits_{i=1}^{n}c_i \cdot x_i$

Bellmanova enačba:

$G(i, W) = max\{G(i-1, W), G(i-1, W - v_i) + c_i\}$

$G(i, W)$ nam pove maksimalno vrednost nahrbtnika za prvih $i$ predmetov in $W$ enot prostora. Paziti pa moramo, da nimamo negativne velikosti $G(0, W) = \begin{cases} -\infty;\ w < 0\\ 0;\ w \ge 0 \end {cases}$

Ustvarimo množici s $S_i$ in $Z_i$

$S_i$ - je množica parov za prvih i-predmetov

$Z_i$ - je množica parov za prvih i-predmetov, kjer vzamemo i-ti predmet

### Naloga 1

Rešujemo problem 0/1 nahrbtnika. Dani so predmeti:

| i | Velikost | Vrednost|
| :-: | :-: | :-: |
| 1 | 11 | 6 |
| 2 | 40 | 9 |
| 3 | 16 | 4 |
| 4 | 32 | 7 |
| 5 | 45 | 6 |
| 6 | 48 | 7 |
| 7 | 9 | 5 |
| 8 | 44 | 9 |


```
S0 = [(0, 0)]
Z1 = [(11, 6)]
S1 = [(0, 0), (11, 6)]
Z2 = [(40, 9), (51, 15)]
S2 = [(0, 0), (11, 6), (40, 9), (51, 15)]
Z3 = [(16, 4), (27, 10), (56, 13), (67, 19)]
S3 = [(0, 0), (11, 6), (27, 10), (51, 15), (67, 19)]
Z4 = [(32, 7), (43, 13), (59, 17), (83, 22), (99, 26)]
S4 = [(0, 0), (11, 6), (27, 10), (43, 13), (51, 15), (59, 17), (67, 19), (83, 22), (99, 26)]
Z5 = [(45, 6), (56, 12), (72, 20), (88, 19), (96, 21), (104, 23), (112, 25), (128, 28),(144, 32)]
S5 = [(0, 0), (11, 6), (27, 10), (43, 13), (51, 15), (59, 17), (67, 19), (83, 22), (99, 26), (128, 28), (144, 32)]
Z6 = [(48, 7), (59, 13), (75, 17), (91, 20), (99, 22), (107, 24), (115, 26), (131, 29), (147, 33), (176, 35), (192, 39)]
S6 = [(0, 0), (11, 6), (27, 10), (43, 13), (51, 15), (59, 17), (67, 19), (83, 22), (99,
26), (128, 28), (131, 29), (144, 32), (147, 33), (176, 35), (192, 39)]
Z7 = [(9, 5), (20, 11), (36, 15), (52, 18), (60, 20), (68, 22), (76, 24), (92, 27), (108, 31), (137, 33), (140, 34), (153, 37), (156, 38), (185, 40), (201, 44)]
S7 = [(0, 0), (9, 5), (11, 6), (20, 11), (36, 15), (52, 18), (60, 20), (68, 22), (76, 24), (92, 27), (108, 31), (137, 33), (140, 34), (153, 37), (156, 38), (185, 40), (201, 44)]
Z8 = [(44, 9), (53, 14), (55, 15), (64, 20), (80, 24), (96, 27), (104, 29), (112, 31), (120, 33), (136, 36), (152, 40), (181, 42), (184, 43), (197, 46), (200, 47), (229, 49), (245, 53)]
S8 = [(0, 0), (9, 5), (11, 6), (20, 11), (36, 15), (52, 18), (60, 20), (68, 22), (76, 24), (92, 27), (104, 29), (108, 31), (120, 33), (136, 36), (152, 40), (181, 42), (184, 43), (197, 46), (200, 47), (229, 49), (245, 53)]
```

*O:* Pri prepisu množice Z5 je pri natanko enem paru prišlo do napake. Kateri par je napačen in kakšen bi moral biti? Opiši, kako lahko napako ugotovimo, ne da bi šli Z5 računati na novo.

*A:* Napaka je pri (72, 20). To lahko ugotovimo tako, da primerjamo naslednje 3 zaproedne pare: (56, 12), (72, 20), (88, 19). Če gledamo 2. element para, kar nam predstavlja ceno, lahko opazimo da gre cena iz 12 na 20, nato pa na 19, kar pa ni v redu. Par (72, 20) bi moral biti (72, 16), saj ima 5. predmet velikost 45, nato pa pogledamo v S4 par, ki ima velikost vzetih predmetov 27. Vrednost tistega narhbtnika je 10 in ker smo vzeli 5. predmet, moramo prišteti še vrednost tega predemta in tako dobimo 16. Napako lahko opazimo tako, da preverimo ali oba elemnta v paru naraščata.

*O:* Če imamo na voljo 160 enot prostora, kakšna je optimalna vrednost nahrbtnika? 

*A:* Imamo 8 predmetov, zato moramo pogledati v S8 in najdemo par (152, 40). To pa nam pove, da nahrbntik z 160 enot prostora lahko zapolnemo z 152 enotami prostora in vrednosta nahrbtnika je 40.

*O:* Koliko neizkoriščenega prostora nam ostane, če optimalno napolnimo nahrbtnik velikosti 110 s prvimi petimi predmeti. Kakšna je ta optimalna vrednost polnitve? Opiši vse možne načine, kako dosežemo to optimalno vrednost!

*A:* Sedaj moramo pogledati v S5 in najdemo par (99, 26). Ostane nam 11 enot prostora. Vrednost tega nahrbtnika je 26. To lahko dosežemo tako, da vzamemo prve 4. predmete, 5. predmeta pa ne vzamemo.

*O:* Skiciraj graf funkcije, ki pokaže, kako se v odvisnosti od razpoložljivega prostora spreminja optimalna vrednost nahrbtnika, če imamo na voljo prvih 6 predmetov in 6. predmet moramo dati v nahrbtnik.

*A:* ![Graf odsekoma naraščujoče funkcije](/Datoteke/Vaje%203/graf.png)

*O:* Ugotovili smo, da imamo na voljo še en predmet, in sicer velikosti 15 in vrednosti 4 (torej je na voljo 9 predmetov). Kakšna je optimalna vrednost nahrbtnika, ki ima 180 enot prostora? Opiši vse možne načine, kako dosežemo to optimalno vrednost!

*A:* To naredimo tako, da poiščemo $S_9$ in sicer $Z_9 = S_8 \oplus (15, 4) = [(15, 4), (24, 9), (26, 10), (35, 15), \ldots]$. Nato pa "zlijemo" množici $S_8$ in $Z_9$, da dobimo $S_9$, torej $S_9 = S_8 \cup Z_9 = [(0, 0), (9, 5), (11, 6), (15, 4), \ldots]$. Nato pa v množici $S_9$ najdemo optimalno vrednost nahrbtnika za 180 enot prostora.

## Vaje 3
**Datum**: 1.3.2023

Na teh vajah smo se razdelili v skupine in imeli tekmovanje kdo bo rešil največ podnalog na Tomo-tu v omejenem času.

### 1. Podnaloga 
```python
def optimalni_tovor(predmeti, nosilnost):
    """Vrne najvecjo ceno za nosilnost 'W'."""
    slovar = dict()
    n = len(predmeti)
    def memo(ind, nosilnost):
        """Vrne najboljšo ceno."""
        if nosilnost < 0:
            return (-math.inf)
        if ind >= n:
            return 0
        if (ind, nosilnost) in slovar:
            return slovar[(ind, nosilnost)]
        vzamemo_tovor = memo(ind + 1, nosilnost - predmeti[ind][1]) + predmeti[ind][0]
        ne_vzamemo_tovor = memo(ind + 1, nosilnost)
        boljsi = max(ne_vzamemo_tovor, vzamemo_tovor)
        slovar[(ind, nosilnost)] = boljsi
        return slovar[(ind, nosilnost)]
    return memo(0, nosilnost)
```

### 3. Podnaloga 
```python
def optimalni_tovor_zaloga(predmeti, nosilnost):
    '''Vrne najvecjo skupno ceno, ki jo lahko trgovec natovori'''
    # opt_cena = optimalni_tovor(predmeti, nosilnost)
    return optimalni_tovor(pomnozi(predmeti), nosilnost)
    
def pomnozi(tab):
    nova_tab = []
    for oklepaj in tab:
        for _ in range(oklepaj[2]):
            nova_tab.append(oklepaj[:2])
    return nova_tab
```

### 4. Podnaloga 
```python
def cena_na_volumen(element):
    """Izračuna ceno na volumen."""
    return element[0] / element[1]

def neomejena_zaloga(predmeti, W):
    urejeni = sorted(predmeti, key=cena_na_volumen, reverse=True)
    cena = 0
    for element in urejeni:
        while W - element[1] > 0:
            cena += element[0]
            W -= element[1]
    return cena 
```

### 6. Podnaloga 
```python
from functools import lru_cache

def tovor_rezanje(predmeti, W):
    """Vrne največjo skupno ceno za nosilnost 'W', pri čemer predemete lahko režemo."""
    @lru_cache(maxsize=None)
    def max_cena(i, w):
        if w < 0:
            return float("-inf")
        if i == 0 or w == 0:
            return 0
        c = predmeti[i-1][0]
        v = predmeti[i-1][1]
        return max(c + max_cena(i-1, w-v), max_cena(i-1, w), c/2 + max_cena(i-1, w-v/2), c/3 + max_cena(i-1, w-v/3), c/4 + max_cena(i-1, w-v/4))

    return round(max_cena(len(predmeti), W),2)
```

## Vaje 4
**Datum**: 8.3.2023

Na vajah smo se spomnili problema matričnega množenja. Zapisali smo Bellmanovo enačbo.

### Naloga 0

Vhodni podatki so matrike in njihove dimenzije $A_1, A_2, \ldots, A_n$ in $[d_1, d_2, \ldots, d_{n+1}]$, kjer je $dim\ A_i = d_i \times d_{i+1}$.

Izhodni podatek je minimalno število množenj realnih števil, ki jih potrebujemo za dane matrike $A_1, A_2, \ldots, A_n$.

$N(i, j)$ nam pove minimalno število množenj realnih števil za $A_i, \ldots, A_j$, izračunamo pa $\displaystyle N(i, j) = \min_{i\ <\ k\ \le\ j}\{N(i, k) + N(k+1, j) + d_i \cdot d_{i+1} \cdot d_j \}$

$N(i, i) = 0$

i \ j | 1 ${(3\times 5)}$ | 2 ${(5\times 4)}$ | 3 ${(4\times 2)}$ | 4 ${(2\times 3)}$ | 5 ${(3\times 5)}$ | 6 ${(5\times 4)}$ | 7 ${(4\times 6)}$ | 8 ${(6\times 3)}$ |
:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
1|0|60 ${(1)}$|70 ${(1)}$|88 ${(3)}$|130 ${(3)}$|164 ${(3)}$|224 ${(3)}$|242 ${(3)}$|
2| |0|40 ${(2)}$|70 ${(3)}$|120 ${(3)}$|150 ${(3)}$|218 ${(3)}$|224 ${(3)}$|
3| | |0|24 ${(3)}$|70 ${(3)}$|102 ${(3)}$|166 ${(3)}$|178 ${(3)}$|
4| | | |0|30 ${(4)}$|70 ${(5)}$|118 ${(6)}$|154 ${(7)}$|
5| | | | |0|60 ${(5)}$|132 ${(6)}$|168 ${(6)}$|
6| | | | | |0|120 ${(6)}$|132 ${(6)}$|
7| | | | | | |0|72 ${(7)}$|
8| | | | | | | |0|

### Naloga 1

Recimo, da imamo izračunano tabelo $N(i,j) = (v, idx)$ iz Bellmanove enačbe, kjer je $v$ optimalno število operacij, $idx$ pa je seznam indeksov $k$, kjer je bil dosežen minimum pri združevanju podproblemov. Kako bi izračunal število vseh optimalnih produktov? Kakšna je časovna zahtevnost? Kaj pa če bi želel izpisati vse optimalne produkte?

Optimalni produkt dobimo po spodnji formuli: 

$O(i, j) = \sum_{k \in N(i,j)} O(i, k) \cdot O(k+1, j)$, pri tem vemo, da je $O(i, i) = 1$ in $O(i, i+1) = 1$.

Časovna zahtevnost je $O(n^3)$, pri tem je  število stanj enako $O(n^2)$ in izračun stanja je zahtevnosti $O(n)$.

### Naloga 2

i \ j | ${(16\times 9)}$ | ${(9\times 3)}$ | ${(3\times 18)}$ | ${(18\times 7)}$ | ${(7\times 12)}$ | ${(12\times 5)}$ | ${(5\times 15)}$ | ${(15\times 5)}$ |
:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
${16\times 9}$|0|432 ${(1)}$|1296 ${(2)}$|1146 ${(2)}$|1638 ${(2)}$|1482 ${(2)}$|2187 ${(2)}$|1932 ${(3)}$|
${9\times 3}$| |0|486 ${(2)}$|567 ${(2)}$|954 ${(2)}$|945 ${(2)}$|1440 ${(2)}$|1395 ${(2)}$|
${3\times 18}$| | |0|378 ${(3)}$|630 ${(4)}$|810 ${(5)}$|1035 ${(6)}$|1260 ${(6, 7)}$|
${18\times 7}$| | | |0|1512 ${(4)}$|1050 ${(4)}$|2400 ${(6)}$|1600 ${(4)}$|
${7\times 12}$| | | | |0|420 ${(5)}$|945 ${(6)}$|970 ${(6)}$|
${12\times 5}$| | | | | |0|900 ${(6)}$|675 ${(6)}$|
${5\times 15}$| | | | | | |0|375 ${(7)}$|
${15\times 5}$| | | | | | | |0|

$Q:$ Koliko je optimalno število operacij? Na kakšne načine lahko zmnožimo te matrike, da imamo toliko operacij?

$A:$ Optimalno število operacij je 1932. Te matrike lahko zmnožimo na dva načina in sicer lahko jih zmnožimo $(A_1 \cdot A_2) \cdot (((A_3 \cdot A_4) \cdot A_5) \cdot A_6 ) \cdot (A_7 \cdot A_8)$ ali pa jih zmnožimo $(A_1 \cdot A_2) \cdot (((((A_3 \cdot A_4) \cdot A_5) \cdot A_6 ) \cdot A_7) \cdot A_8)$.

### Naloga 3

Podano imamo naslednjo tabelo:

i \ j | 1 ${(3\times 5)}$ | 2 ${(5\times 4)}$ | 3 ${(4\times 2)}$ | 4 ${(2\times 3)}$ | 5 ${(3\times 5)}$ | 6 ${(5\times 4)}$ | 7 ${(4\times 6)}$ | 8 ${(6\times 3)}$ |
:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
1|0|60 ${(1)}$|70 ${(1)}$|88 ${(3)}$|130 ${(3)}$|164 ${(3)}$|224 ${(3)}$|242 ${(3)}$|
2| |0|40 ${(2)}$|70 ${(3)}$|120 ${(3)}$|150 ${(3)}$|218 ${(3)}$|224 ${(3)}$|
3| | |0|24 ${(3)}$|70 ${(3)}$|102 ${(3)}$|166 ${(3)}$|178 ${(3)}$|
4| | | |0|30 ${(4)}$|70 ${(5)}$|118 ${(6)}$|154 ${(7)}$|
5| | | | |0|60 ${(5)}$|132 ${(6)}$|168 ${(6)}$|
6| | | | | |0|120 ${(6)}$|132 ${(6)}$|
7| | | | | | |0|72 ${(7)}$|
8| | | | | | | |0|

$Q:$ Koliko operacij potrebujemo, da jih optimalno zmnožimo?

$A:$ Da optimalno zmnožimo matrike od 1 do 8 pogledamo v 1. vrstico in 8 stolpec in ugotovimo, da potrebujemo 242 množenj realnih števil.

$Q:$ Kako jih mormao množiti?

$A:$ Zmnožiti moramo $(A_1 \cdot (A_2 \cdot A_3)) \cdot ((((A_4 \cdot A_5) \cdot A_6) \cdot A_7) \cdot A_8)$.

$Q:$ Kako optimalno zmnožimo matrike od 3 do 7?

$A:$ Pogledamo 3. vrstico in 7. stolpec, ki nam pove da jih moramo zmnožiti $A_3 \cdot ((A_4 \cdot A_5) \cdot A_6) \cdot A_7$.

$Q:$ Koliko operacij potrebujemo, da optimalno zmnožimo prvih 5 matrik?

$A:$ Pogledamo 1. vrstico in 5. stolpec, ki nam pove, da potrebujemo 130 množenj realnih števil.

$Q:$ Kako naj zmnožimo zadnje štiri matrike, da bo število operacij najmanjše?

$A:$ Pogledamo 5. vrstico in 8. stolpec, ki nam pove da jih moramo zmnožiti $(A_5 \cdot A_6) \cdot (A_7 \cdot A_8)$.

$Q:$ Ali si lahko pomagamo z izračunanimi podatki, če spremenimo število stolpcev zadnje matrike iz 3 na 4, da izračunamo novo optimalno množenje? Kaj moramo narediti?

$A:$ Morali bi izračunati cel zadnji stolpec, kar pa pomeni, da bi morali ponovno izračunati celotno tabelo.