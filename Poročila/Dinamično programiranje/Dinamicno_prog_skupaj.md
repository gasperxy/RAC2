# <center> Vaje 1 </center>
## Datum: 15.2.
___
___

## <ins>Časovna zahtevnost</ins>

Kaj pomeni $ f \in O(g)$ za neki funkciji $ f,g: \mathbb{N} \to  \mathbb{R}^{+}$ ?

$f \in O(g) \iff \exists c \ \exists n_{0}: \forall n \geq n_{0},\ f(n) \leq c \ast g(n) $

<img src=graf_prvi.png  width="60%" height="60%"> 

|  | dodaj(n) | dodaj(i) | dodaj(0) | dostop(i) | "x in" | briši(0)| briši(i) | briši(n) |
|-- | :--:| :--:| :--: | :--: | :--: | :--:|:--:| :--:|
seznam | O(1)|O(n)|O(n)|O(1)|O(n)|O(n)|O(n)|O(1)
slovar/mn| O(1)|O(1)|O(1)|O(1)|O(1)|O(1)|O(1)|O(1)
verižni seznam | O(1)/O(n)|O(1)/O(n)|O(1)/O(n)|O(n)|O(n)|O(1)/O(n)|O(1)/O(n)|O(1)/O(n)

___
___
## <ins>Žabica</ins>

$muhe[i]$ = število muh na i-tem mestu

`žabica(i,e)` = to je minimalno število skokov, da pridemo iz močvirja, če se nahajamo na `i`-tem  lokvanu in imamo `e` energije

$žabica(i,e) = 1 + \left\{
\begin{array}{ll}
0 &\text{, če } i + e > n \\ 
\min\limits_{d \in(1, \dots,e)}(žabica(i+d,e-d+muhe[i+d])) &\text{, sicer}
\end{array} 
\right.
$

### *Robni pogoji*: 
    
&nbsp;&nbsp;&nbsp;&nbsp; $žabica(i,e) = 0 ; \ i > n$

&nbsp;&nbsp;&nbsp;&nbsp; $žabica(i,e) = 1 ; \ e > n-i$

### *Časovna zahtevnost*:
Izračunati moramo vsa stanja:
- število stanj(kombinacije $(i,e)$): $O(n^2)$
- čas za izračun enega stanja: $O(n)$

 $\Longrightarrow  O(n^2) * O(n)= O(n^3)$ 

___ 
___
<br>

# <center> Vaje 2 </center>
## Datum: 22.2.
___
___

## <ins>Ponovitev 0/1 nahrbtnika</ins>

Vhod:
- predmeti $(v_i,c_i)$ za $i = 1,\dots,n$
- velikost nahrbtnika $W$

Izhod:

- $ x = (x_1,\dots,x_n); \ x_i = \left\{
\begin{array}{ll}
1 &\text{, vzamemo i-ti predmet} \\ 
0 &\text{, sicer}
\end{array} 
\right.
$

    tako da $\sum\limits_{i=1}^n v_i \cdot x_i \leq W$ in $\sum\limits_{i=1}^n c_i \cdot x_i$ maksimalna možna

____
$G(i,w)=$ maksimalna vrednost  nahrbnika, z predmeti $1,\dots,i$ in velikostjo $w$.

$G(i,w)= max(G(i-1,w),G(i-1,w-v_i) + c_i)$\
$+$ robni pogoji

$G(i,w)$ gledamo kot funkcijo spremenljivke $w$ 

<img src=graf_2.png  width="60%" height="60%"> 

$S_i \dots$ opisuje $G(i,.)$\
$Z_i \dots$ opisuje $G(i,.)$, pri čemer $i$-ti predmet vzamemo\
$Z_i \dots$ "$S_{i-1} \ddagger (v_i,c_i)$"\
$S_i \dots$ "zlitje $S_{i-1}$ in $Z_i$"
___
___
## Primer
### <ins>Vprašanje 1 </ins>
```
Pri prepisu množice je pri natanko enem paru prišlo do napake. Kateri par je napačen in kakšen bi moral biti? Opiši, kako lahko napako ugotovimo, ne da bi šli Z5 računati na novo.
```
$5.$ predmet: (45, 6)\
$Z_5 = S_4 \ddagger (45,6)$\
$Z_5= [(45,6),(56,12),\color{red}{(72,16)}\color{white}{,\dots}]$ <br>
Brez računanja $Z_5$ bi lahko ugotovili tako, da bi preverili če je
$Z_5$ naraščajoča

### <ins>Vprašanje 2</ins>
```
Če imamo na voljo 160 enot prostora, kakšna je optimalna vrednost nahrbtnika?
```
V $S_8$ pogledamo zadnji (manjši) par $(w,c)$ tako, da
je $w \leq 160$.<br>
Tak par je $(152,40)$. Optimalna vrednost je 40.

### <ins>Vprašanje 3</ins>
```
Koliko neizkoriščenega prostora nam ostane, če optimalno napolnimo nahrbtnik velikosti 110 s prvimi petimi predmeti. Kakšna je ta optimalna vrednost polnitve? Opiši vse možne načine, kako dosežemo to optimalno vrednost!
```
$w = 110$, $i = 5$ 

Par iz $S_5$ (99,26) tako, da ostane neizkoriščenega prostora 11,
optimalna vrednost je 26.

|i|  par| je v $Z_i$ | je v $S_i$ | $x_i$|
|:--:| :--:|:--:|:--:|:--:|
5|(99,26)| 0| 0 | $x_5=0$|
4|(99,26)| 1|0| $x_4 = 1$|
3|(67,19)| 1| 0 | $x_3=1$|
2|(51,15)| 1|0| $x_2 = 1$|
1|(11,6)|1 |0|$x_1 = 1$|

Torej $x = [1,1,1,1,0]$


### <ins>Vprašanje 4</ins>
```
Skiciraj graf funkcije, ki pokaže, kako se v odvisnosti od razpoložljivega prostora spreminja optimalna vrednost nahrbtnika, če imamo na voljo prvih 6 predmetov in 6. predmet moramo dati v nahrbtnik.
```
Opazovati moramo $Z_6$, ker 6 elementov vzamemo

<img src=graf.png  width="60%" height="60%">

### <ins>Vprašanje 5</ins>
```
Ugotovili smo, da imamo na voljo še en predmet, in sicer velikosti 15 in vrednosti 4 (torej je na voljo 9 predmetov). Kakšna je optimalna vrednost nahrbtnika, ki ima 180 enot prostora? Opiši vse možne načine, kako dosežemo to optimalno vrednost!
```
Novi predmet (15,4) <br>
Optimalna vrednost nahrbtnika z 180 enot prostora<br>
$G(9,180)=?$

_Prvi način:_

&nbsp;&nbsp;&nbsp;&nbsp; $Z_9=S_8\ddagger(15,4) = [(15,4),(24,9),(26,10),\dots]$<br>
&nbsp;&nbsp;&nbsp;&nbsp; $S_9 = S_8 \uplus Z_9$

_Drugi način:_

&nbsp;&nbsp;&nbsp;&nbsp; $G(8,180)= max(G(8,180),G(8,165)+4)$

&nbsp;&nbsp;&nbsp;&nbsp; Iz $S_8$ razberemo:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $G(8,180)=40$<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $G(8,165)+4=44$<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;$\implies G(9,180)=44$



|i|  | je v $Z_i$ | je v $S_i$ | x|
| :--:|:--:|:--:|:--:|:--:|
9|(167,44)| 0| 0 | $x_9=1$|
8|(152,40)| 1|0| $x_8 = 1$|
7|(108,31)| 1| 0 | $x_7=1$|
6|(99,26)| 0|1| $x_6 = 0$|
5|(99,26)| 0| 0 | $x_5=0$|
4|(99,26)| 1|0| $x_4 = 1$|
3|(67,19)| 1| 0 | $x_3=1$|
2|(51,15)| 1|0| $x_2 = 1$|
1|(11,6)|1 |0|$x_1 = 1$|


Torej $x = [1,1,1,1,0,0,1,1,1]$

___
___
## <ins>Naloga 2</ins>

seznam = $[3,34,4,12,5,2]$, $S=9$ <br>
Ali lahko $S$ zapišemo kot vsoto števil iz seznama?

<ins>Prvi način (dinamično):</ins>

&nbsp;&nbsp;&nbsp;&nbsp; $ vsota(i,S) = \left\{
\begin{array}{ll}
true &\text{, če S lahko zapišemo kot vsoto z [s\_1,\dots,s\_n]} \\ 
false &\text{, sicer}
\end{array} 
\right.
$

&nbsp;&nbsp;&nbsp;&nbsp; $ vsota(i,S)= vsota(i-1,S-s_i) \lor  vsota(i-1,S) $

&nbsp;&nbsp;&nbsp;&nbsp; Robni pogoji:<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $vsota(i,S)=true \dots S_i = S$ <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $vsota(0,0)=true $ <br> 
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; $vsota(i,0)=false, \ i > 0$ <br> 

\
<ins>Drugi način:</ins> \
Uporabimo podobno idejo kot pri 0/1 nahrbtniku. Imamo nek nabor, kjer so shranjene do sedaj vse možne vsote in nek drug nabor, kjer hranimo nove kandidate. Naredimo unijo naborov in tako dodamo nove kadidate. Postopek ponovimo za vsak element osnovnega seznama, z izjemo prvega.

Koda:
```
tab2 = [2,3,4,5,12,34]
rez = {tab2[0]}
for el in tab2[1:]:
    nove=set()
    for delna in rez:
            nove.add(delna+el)
    rez.update(nove)
    rez.add(el)
print(rez)
```
---
---
<br>

# <center> Vaje 3 </center>

## Datum: 1.3.
___
___

## Naloga 1
*Implementiraj funkcijo `optimalni_tovor(predmeti, W)`, ki vrne največjo skupno ceno predmetov, ki jih lahko trgovec natovori na letalo z maksimalno nosilnostjo `W`.*

```
def optimalni_tovor(predmeti, W):
    @lru_cache(maxsize=None)
    def najboljsi(i, W):
        if W < 0:
            return float("-inf")
        if W == 0 or i == 0:
            return 0
        return max(najboljsi(i-1,W), najboljsi(i-1,W-predmeti[i-1][1])+predmeti[i-1][0])
    return najboljsi(len(predmeti),W)
```
---
## Naloga 2

*Implementiraj funkcijo `optimalni_predmeti(predmeti, W)`, ki vrne seznam predmetov ki dosežejo največjo vrednost, če lahko na letalo natovorimo skupno težo največ `W`. Če je možnosti več, vrni katerokoli.*


```
def optimalni_predmeti(predmeti, W):
    predmeti = [(el[1],el[0]) for el in predmeti]
    n = len(predmeti)
    # matrika kjer hranimo vrednosti za vsak predmet in težo
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, W + 1):
            # preverimo če trenutni predmet gre v nahrbtnik
            if predmeti[i-1][0] <= j:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-predmeti[i-1][0]] + predmeti[i-1][1])
            else:
                dp[i][j] = dp[i-1][j]

    # preverimo katere predmete smo vzeli
    selected = list()
    j = W
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i-1][j]:
            selected.append(predmeti[i-1])
            j -= predmeti[i-1][0]
    
    selected = [(el[1],el[0]) for el in selected]
    return selected
```
---
## Naloga 3

*Trgovec je dobil dodatno pošiljko obstoječih predmetov. Tako ima sedaj na razpolago več kot en predmet posameznega tipa. Predmete tako predstavimo s seznamom elementov oblike
$(c_i, v_i, z_i)$, kjer je:*
* $c_i$  cena
* $v_i$ teža
* $z_i$ zaloga
* $i$-tega predmeta.



```
def optimalni_tovor_zaloga(predmeti, W):
    nova = [(el[0],el[1]) for el in predmeti for _ in range(el[2])]
    return optimalni_tovor(nova,W)
```
___
## Naloga 4

Predpostavi, da ima sedaj trgovec na voljo neomejeno zalogo posameznih predmetov. implementiraj funkcijo `neomejena_zaloga(predmeti, W)`, ki vrne najvišjo skupno ceno tovora na letalu z maksimalno nosilnostjo `W`

```
def neomejena_zaloga(p,W):
    @lru_cache(maxsize=None)
    def pom(w):
        if w == 0:
            return 0
        return max([pom(w-v)+c for (c,v) in p if v <= w]+[0])
    return pom(W)
```

---
---
<br>

# <center> Vaje 4 </center>

## Datum: 8.3.
___
___

## <ins>Naloga 0</ins>
### Vhod: 
- matrike $[A_{1},\dots,A_{n}]$
- dimenzije  $[d_{1},\dots,d_{n+1}]$
    
  pri čemer $A_{i} = d_{i} \times d_{i+1}$

### Izhod:
- minimalno število množenj realnih števil za izračun produkta danih matrik $A_{1} \cdot A_{2} \cdots A_{n}$

### Bellmanova enačba oz. rekurzivna zveza:
- $N(i,j)$ = minimalno število množenj realnih števil za izračun produkta matrik $A_{i} \cdot A_{i+1} \cdots A_{j}$
- $N(i,j) = \min\limits_{i \le k <j}\{N(i,k)+N(k+1,j) + d_{i} \cdot d_{k+1} \cdot d_{j}\}$

### Primer:
| |1<br>$3\times 5$|2<br>$5\times 4$|3<br>$4\times 2$|4<br>$ 2\times 3$ |5<br>$ 3\times 5$ |6<br>$ 5\times 4$ |7<br>$ 4\times 6$ |8<br>$ 6\times 3$ |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--:|
$3\times 5$|  $0$| $60$ | $70_{1}$|$88_{3}$ |$130_{3}$ |$164_{3}$|$224_{3}$|$242_{3}$|
$5\times 4$ |  | $0$| $40$|$70_{3}$|$120_{3}$|$150_{3}$|$218_{3}$|$224_{3}$|
$4\times 2$|||$0$|$24$|$70_{3}$|$102_{3}$|$166_{3}$|$178_{3}$|
$2\times 3$ ||||$0$|$30$|$70_{5}$|$118_{6}$|$154_{7}$|
$3\times 5$ |||||$0$|$60$|$132_{6}$|$168_{6}$|
$5\times 4$ ||||||$0$|$120$|$132_{6}$
$4\times 6$ |||||||$0$|$72$
$6\times 3$ ||||||||$0$

$N(1,3)= min(0 + 40 + 3\cdot5\cdot2,\ 60+0+3\cdot4\cdot2)=70$

$N(2,4)=min(0+24+5\cdot4\cdot3,\ 40+0+5\cdot2\cdot3)=70$

$N(3,5)=min(0+30+4\cdot2\cdot5,\ 24+0+4\cdot3\cdot5)=70$

$N(4,6)=min(0+60+2\cdot3\cdot4,\ 30+0+2\cdot5\cdot4)=70$

$N(5,7)=min(0+120+3\cdot5\cdot6,\ 60+0+3\cdot4\cdot6)=132$

$N(6,8)=min(0+72+5\cdot4\cdot3,\ 120+0+5\cdot6\cdot3)=132$

---
---
## <ins>Naloga 1</ins>

*Recimo, da imamo izračunano tabelo ***N(i,j) = (v, idx)*** iz Bellmanove enačbe, kjer je v optimalno število operacij, ***idx*** pa je seznam indeksov ***k***, kjer je bil dosežen minimum pri združevanju podproblemov. Kako bi izračunal število vseh optimalnih produktov? Kakšna je časovna zahtevnost? Kaj pa če bi želel izpisati vse optimalne produkte?*


$O(i,j)=število \ optimalnih \ produktov \ matrik \ A_{i}\cdot A_{i+1}\cdots A_{j}$


$O(i,j)=\sum\limits_{k \in N(i,j)[1]\sim idx} O(i,k)\cdot O(k+1,j)$

Časovna zahtevnost $O(n^3)\ \dots \ $($n^2$-število stanj, $n$-izračun stanja)



___
___
## <ins>Naloga 2</ins>
Podano imamo matriko:

<img src=mnozenje.png  width="60%" height="60%">


```
Koliko je optimalno število operacij? 
```
Optimano število operacij preberemo iz prve vrstice in zadnjega stolpca.
Torej $N(1,8)=1932$

```
Na kakšne načine lahko zmnožimo te matrike, da imamo toliko operacij?
```
Zmnožimo lahko na dva načina. Torej:
- $(A_{1}\cdot A_{2})\Big(\big(((A_{3}\cdot A_{4})A_{5})A_{6}\big)(A_{7}\cdot A_{8})\Big)$ 

- $(A_{1}\cdot A_{2})\Big(((((A_{3}\cdot A_{4})A_{5})A_{6})A_{7})A_{8}\Big)$

V splošnem dobimo: Binarno drevo z $n$ listi $\longleftrightarrow$ Izraz z $n$ členi in pravilno postavljenemi oklepaji $\longleftrightarrow$ Catalanovo število

___
___
## <ins>Naloga 3</ins>

<img src=mnozenje2.png  width="60%" height="60%">

```
Koliko operacij potrebujemo, da jih optimalno zmnožimo?
```
Potrebujemo 242 operacij, torej $N(1,8)$.

```
Kako jih moramo množiti?
```
Množimo jih po naslednjem vrstnem redu $((A_{1}\cdot A_{2})A_{3})\Big(\big(((A_{4}\cdot A_{5})A_{6})A_{7}\big)A_{8}\Big)$ 

```
Kako optimalno zmnožimo matrike od 3 do 7?
```

Množimo jih po naslednjem vrstnem redu $A_{3}\Big(\big((A_{4}\cdot A_{5})A_{6}\big)A_{7}\Big)$

```
Koliko operacij potrebujemo, da optimalno zmnožimo prvih 5 matrik?
```

Potrebujemo $N(1,5)=130$ operacij

```
Kako naj zmnožimo zadnje štiri matrike, da bo število operacij najmanjše?
```

Število operacij bo $N(5,8)=168$. Zmnožimo jih po naslednjem vrstnem redu $(A_{5}\cdot A_{6})(A_{7}\cdot A_{8})$

```
Ali si lahko pomagamo z izračunanimi podatki, če spremenimo število stolpcev zadnje matrike iz 3 na 4, da izračunamo novo optimalno množenje? Kaj moramo narediti?
```
Da lahko si pomagamo. Zadnji stolpec bi poračunali še enkrat od spodaj navzgor. Časovna zahtevnost bi bila $O(n^2)$.


___
___
___
<br> 

# <center> Časovna zahtevnost </center>

## Koda
```
def optimalni_tovor(predmeti, W):
    @lru_cache(maxsize=None)
    def najboljsi(i, W):
        if W < 0:
            return float("-inf")
        if W == 0 or i == 0:
            return 0
        return max(najboljsi(i-1, W), najboljsi(i-1, W-predmeti[i-1][1])+predmeti[i-1][0])
    return najboljsi(len(predmeti), W)

```


Časovna zahtevnost zgonje kode je $O(n\cdot w)$, kjer je `n` število vseh predmetov, `w` pa volumen nahrbtnika.
Predstavljamo si lahko, kot da polnimo tabelo, ki ima $n$ predmetov in volumne nahrbtnika od $1$ do $w$. Torej teh polj je ravno $n \cdot w$. 

---
## Grafični prikaz

Prikazano je različno naraščanje skupnega volumna in števila predmetov. V legendi je opisano naraščanje posameznega parametra.

Časovne zahtevnosti,ki smo jih želeli prikazati:
-  linearno 
- log-linearno
- kvadratično

<img src=cas_zahtevnost.png width="60%" height="60%"> 

Potreben čas[s] v odvisnoti od števila predmetov

___
Za risanje smo uporabili naslednjo kodo:

```
from functools import lru_cache
import matplotlib.pyplot as plt
import time
import math

# Časovna zahtevnost O(n*W)

def optimalni_tovor(predmeti, W):
    @lru_cache(maxsize=None)
    def najboljsi(i, W):
        if W < 0:
            return float("-inf")
        if W == 0 or i == 0:
            return 0
        return max(najboljsi(i-1,W), najboljsi(i-1,W-predmeti[i-1][1])+predmeti[i-1][0])
    return najboljsi(len(predmeti),W)

x1 = []
y1 = []

for i in range(2,30,2):
    predmeti = [(2,3) for _ in range(i*10)]
    volumen = 14*i
    skupaj=0
    for _ in range(100):
        zacetek = time.time()
        optimalni_tovor(predmeti,volumen)
        konec = time.time()
        skupaj+=konec-zacetek
    x1.append(len(predmeti))
    y1.append(skupaj/100)

x2 = []
y2 = []

for i in range(2,50,3):
    predmeti = [(2,3) for _ in range(i*10)]
    volumen = 14*math.log(i)
    skupaj=0
    for _ in range(100):
        zacetek = time.time()
        optimalni_tovor(predmeti,volumen)
        konec = time.time()
        skupaj+=konec-zacetek
    x2.append(len(predmeti))
    y2.append(skupaj/100)

x3 = []
y3 = []

for i in range(2,50,3):
    predmeti = [(2,3) for _ in range(i*10)]
    volumen = 35
    skupaj=0
    for _ in range(100):
        zacetek = time.time()
        optimalni_tovor(predmeti,volumen)
        konec = time.time()
        skupaj+=konec-zacetek
    x3.append(len(predmeti))
    y3.append(skupaj/100)
      
plt.plot(x3,y3,label = "st. predmetov: lin\n volumen: konst.")
plt.plot(x2,y2,label = "st. predmetov: lin\n volumen: log.")
plt.plot(x1,y1,label = "st. predmetov: lin\n volumen: lin.")

plt.title("Časovna zahtevnost\nRazlično naraščanje parametrov")
plt.legend()
# plt.savefig("cas_zahtevnost.pdf")
plt.show()
```






