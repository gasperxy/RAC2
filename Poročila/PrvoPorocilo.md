# Prvo poročilo za Računalništvo 2
**Ime:** Gregor Kuhelj


# Vaje 1
**Datum**: 15.2.2023

Na vajah smo osvežili znanje iz Računalništva 1 o časovnih zahtevnostih.
Prikaz časovnih zahtevnosti za različne operacije nad seznami, množicami/slovarji ter verižnimi seznami je naslednji:

### Naloga 1

| Operacija            | Seznam          | Množica / slovar| Verižni seznam   |
| :--------:           | :-------------: | :------------:  | :------------:   | 
| dodaj (na konec)     | $O(1)$          | $O(1)$          | $O(1)$ / $O(n)$  |
| dodaj (na sredino)   | $O(n)$          | $O(1)$          | $O(1)$ / $O(n)$  | 
| dodaj (na začetek)   | $O(n)$          | $O(1)$          | $O(1)$ / $O(n)$  | 
| dostop               | $O(1)$          | $O(1)$          | $O(n)$           | 
| $x$ (vsebovan)       | $O(n)$          | $O(1)$          | $O(n)$           | 
| briši (na začetku)   | $O(n)$          | $O(1)$          | $O(1)$ / $O(n)$  | 
| briši (na sredini)   | $O(n)$          | $O(1)$          | $O(1)$ / $O(n)$  | 
| briši (na koncu)     | $O(1)$          | $O(1)$          | $O(1)$ / $O(n)$  |



### Naloga 2
Rešitev naloge 'Žabica' z uporabo rekurzije je naslednja:

```python
def zabica(mocvara):
    """Vrne najmanjše število skokov, da pridemo ven iz močvare.
        Problem reši z memoizacijo."""
    n = len(mocvara)
    def skok(i, e):
        if n == 1:
            return 1
        if i > n:
            return 0
        if (i, e) in slovar:
            return slovar[(i, e)]
        tab = []
        for koliko_skok in range(1, e + 1):
            if i + koliko_skok < n:
                tab.append(skok(i + koliko_skok, e - koliko_skok + mocvara[i + koliko_skok]))
        if len(tab) <= 0:
            return 0
        naj = min(tab) + 1
        slovar[(i, e)] = naj
        return slovar[(i, e)]
    slovar = dict()
    return skok(0, mocvara[0])
```
Rešitev teiste naloge brez uporabe rekurzije (iterativno) je naslednja:

``` python 
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

Primerjava hitrosti med rekurzivno in iterativno kodo:

![](/Datoteke/Vaje1/grafV1.png)


# Vaje 2 (22.2.2023)

Govorili smo o problemu 0/1 nahrbtnika.

Vhodni podatki pri tem problemu so taki pari $(v_i, c_i)$, torej pari velikosti in cene $i$-tega predmeta ($i = 1, 2, \dots, n$).

Izhodni podatek je vektor $X = (x_1,x_2, \dots, x_n)$, ki nam pove, če $i$-ti predmet vzamemo ali ne. Povedano drugače:

$ x_i = \begin{cases}
1;\ vzamemo \ i-ti \ predmet\\ 0;\ ne\ vzamemo\ i-tega\ predemeta
\end{cases}$

Paziti moramo, da skupna velikost predmetov, ki jih bomo dali v nahrbtnik ni večja od kapacitete nahrbtnika $W$. Povedano drugače, veljati mora spodnja enačba:

$$\sum_{i=1}^{n}v_i \cdot x_i \leq W$$


### Bellmanova enačba za problem 0/1 nahrbtnika:


$G(i, W) = max\{G(i-1, W), G(i-1, W - v_i) + c_i\}$

$G(i,W)$ nam pove, kolikšna je največja vrednost nahrbtnika za prvih $i$ predmetov, pri kapaciteti nahrbtnika $W$.

Ne sme se nam zgoditi, da vrednost $G(i,W)$ ne postane negativna, saj bi v tem primeru veljalo, da je kapaciteta nahrbtnika negativna, kar seveda ne more veljati.

Ustvarimo množici s $S_i$ in $Z_i$, kjer je $S_i$ množica parov za prvih $i$ predmetov in $Z_i$ množica parov za prvih $i$ predmetov, kjer vzamemo $i$ - ti predmet




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
| 7 | 9  | 5 |
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

- Pri prepisu množice Z5 je pri natanko enem paru prišlo do napake. Kateri par je napačen in
kakšen bi moral biti? Opiši, kako lahko napako ugotovimo, ne da bi šli Z5 računati na novo.

Napaka je pri elementu $(72,20)$. To vemo po tem, da je element za njim $(88,19)$, kjer lahko opazimo, da je drugo število manjše od predhodnega $(19 < 20)$, kar je narobe, saj morajo biti druge vrednosti v oklepaju naraščajoče.


- Če imamo na voljo 160 enot prostora, kakšna je optimalna vrednost nahrbtnika?

Optiomalna vrednost nahrbtnika je 152. To določimo tako, da pogledamo katera prva številka v oklepaju pri S8 je najbližja 160, pri pogoju, da je manjša od 160. S8 gledamo zato, ker imamo na voljo vseh 8 predmetov.

- Koliko neizkoriščenega prostora nam ostane, če optimalno napolnimo nahrbtnik velikosti
110 s prvimi petimi predmeti. Kakšna je ta optimalna vrednost polnitve? Opiši vse možne
načine, kako dosežemo to optimalno vrednost!

Neizkoriščenega prostora bo 11, saj moramo pogledati največjo vrednost, ki je manjša od 110 v seznamu S5 (saj imamo opravka s prvimi petimi predmeti). Optimalna vrednost je torej $(99,26)$, torej 99. Prve štiri predmete vzamemo, medtem ko petega izpustimo.

- Skiciraj graf funkcije, ki pokaže, kako se v odvisnosti od razpoložljivega prostora spreminja optimalna vrednost nahrbtnika, če imamo na voljo prvih 6 predmetov in 6. predmet moramo dati v nahrbtnik.

![](/Datoteke/Vaje2/graf.png)

- Ugotovili smo, da imamo na voljo še en predmet, in sicer velikosti 15 in vrednosti 4 (torej je
na voljo 9 predmetov). Kakšna je optimalna vrednost nahrbtnika, ki ima 180 enot prostora?
Opiši vse možne načine, kako dosežemo to optimalno vrednost!

Do optimalne rešitve pridemo tako, da poiškemo $S9$ in $Z9$, kjer je $Z_9 = S_8 \oplus (15, 4) = [(15, 4), (24, 9), (26, 10), (35, 15), \ldots]$. Nato pa 'zlijemo' množici $S8$ in $Z9$, s čimer dobimo $S9$. Potem enosdtavno poiščemo optimalno vrednost za vrednost nahrbtnika 180 s postopkom, ki je zapisan v prejšnjih odgovorih na vprašanja.


# Vaje 3 (1.3.2023)

V paru sem bil z Alenom Nemaničem.

Rešitve prvih štirih nalog na Tomu so naslednje:

#### Prva podnaloga:

``` python
import math

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



#### Tretja podnaloga:
``` python
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

#### Četrta podnaloga:
``` python
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

#### Šesta podnaloga:
``` python
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


# Vaje 4 (8.3.2023)

#### Naloga 0
Pri problemu množenja matrik nas zanima, v kakšnem vrstnem redu moramo zmnožiti matrike 
$A_1, A_2, \ldots, A_n$ s pripadajočimi dimenzijami $[d_1, d_2, \ldots, d_{n+1}]$, (kjer je $dim\ A_i = d_i \times d_{i+1}$) da bo število množenj najmanjše možno.

Optimalno rešitev dobimo po naslednji formuli:

$$N(i, j) = \min_{i\ <\ k\ \le\ j}\{N(i, k) + N(k+1, j) + d_i \cdot d_{i+1} \cdot d_j \}$$
Pri tem, nam $N(i,j)$ predstavlja minimalno število množenj matrik od $A_1$ do $A_n$.

Tabela števil množenj za primer velikosti 3x5, 5x4, 4x2, 2x3, 3x5, 5x4, 4x6, 6x3 bi bila naslednja:

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

Minimalno število operacij, ki ga potrebujemo je 242. To je število v skrajno desnem kotu zgornje tabele, ki nam pove, kako na optimalni način zmnožiti matrike od prve do zadnje.


#### Naloga 1
- Recimo, da imamo izračunano tabelo $N(i,j) = (v, idx)$ iz Bellmanove enačbe, kjer je $v$ optimalno število operacij, $idx$ pa je seznam indeksov $k$, kjer je bil dosežen minimum pri združevanju podproblemov. Kako bi izračunal število vseh optimalnih produktov? Kakšna je časovna zahtevnost? Kaj pa če bi želel izpisati vse optimalne produkte?

Optimalni produkt dobimo po spodnji formuli: 

$$ O(i,j) = \sum_{k \in N(i,j)[1]} O(i,k) \cdot O(k+1,j) $$ 
pri tem vemo, da je $O(i,i) = 1$ in $O(i,i+1) = 1$



Časovna zahtevnost je $O(n^3)$, pri tem je  število stanj enako $O(n^2)$ in izračun stanja je zahtevnosti $O(n)$






#### Naloga 2

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

- Koliko je optimalno število operacij? Na kakšne načine lahko zmnožimo te matrike, da imamo toliko operacij?

Optimalno številno operacij je 1932. Optimalna načina množenja sta dva, in sicer lahko zmožimo matrike tako: $(A_1 \cdot A_2) \cdot (((A_3 \cdot A_4) \cdot A_5) \cdot A_6 ) \cdot (A_7 \cdot A_8)$ ali pa tako: $(A_1 \cdot A_2) \cdot (((((A_3 \cdot A_4) \cdot A_5) \cdot A_6 ) \cdot A_7) \cdot A_8)$. 

#### Naloga 3

Podano imamo naslednjo tabelo, ki je tokrat oštevilčena od 0 naprej:

i \ j | 1 ${(3\times 5)}$ | 2 ${(5\times 4)}$ | 3 ${(4\times 2)}$ | 4 ${(2\times 3)}$ | 5 ${(3\times 5)}$ | 6 ${(5\times 4)}$ | 7 ${(4\times 6)}$ | 8 ${(6\times 3)}$ |
:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
1|0|60 ${(1)}$|70 ${(1)}$|88 ${(3)}$|130 ${(3)}$|164 ${(3)}$|224 ${(3)}$|242 ${(3)}$|
2| |0|40 ${(2)}$|70 ${(3)}$|120 ${(3)}$|150 ${(3)}$|218 ${(3)}$|224 ${(3)}$|
3| | |0|24 ${(3)}$|70 ${(3)}$|102 ${(3)}$|166 ${(3)}$|178 ${(3)}$|
4| | | |0|30 ${(4)}$|70 ${(5)}$|118 ${(6)}$|154 ${(7)}$|
5| | | | |0|60 ${(5)}$|132 ${(6)}$|168 ${(6)}$|
6| | | | | |0|120 ${(6)}$|132 ${(6)}$|
7| | | | | | |0|72 ${(7)}$|
8| | | | | | | |0


- Koliko operacij potrebujemo, da jih optimalno zmnožimo?

Potrebujemo 242 operacij (to vidimo iz skrajno desnega zgornjega elementa, ki predstavlja optimalno število operacij za matrike.)

- Kako jih moramo množiti?

Matrike moramo množiti tako: 
$$(A_1 \cdot (A_2 \cdot A_3)) \cdot ((((A_4 \cdot A_5) \cdot A_6) \cdot A_7) \cdot A_8)$$

- Kako optimalno zmnožimo matrike od 3 do 7?

Odgovor na to vprašanje dobimo tako, da pogledamo element v tretji vrstici in v sedmem stolpcu, od koder vidimo, da je optimalni način množenja $ A_3 \cdot ((A_4 \cdot A_5) \cdot A_6) \cdot A_7$.

- Koliko operacij potrebujemo, da optimalno zmnožimo prvih 5 matrik?

Odgovor je 130, saj pogledamo vrednost elementa v 1.vrstici in 5.stolpcu

- Kako naj zmnožimo zadnje štiri matrike, da bo število operacij najmanjše?

Element v 5.vrstici in 8.stolpcu nam pove, da je optimalno množenje tako:
$(A_5 \cdot A_6) \cdot (A_7 \cdot A_8)$.


#### Naloga 4
Na prvem računalniku imamo matrike $A_1$ do $A_4$.

Na drugem računalniku imamo matrike $A_5$ do $A_8$.

Bellmanova enačba za dva računalnika z omejenim dostopom:

$\begin{array}{r}
\tilde{N}(1,8)=\max \left\{N(1,4), N(5,8)+d_1 \cdot d_5 \cdot d_9+\right. 
\left.\min \left\{d_1 d_5, d_s ; d_8\right\}\right)
\end{array}$


Bellmanova enačba za dva računalnika  z neomejenim dostopom:

$\tilde{N}(1,8)=\min _{1 \leqslant k<8}\left\{\max (N(1, k), N(k+1,8))+d_1 d_{k+1} d_9\right\}$