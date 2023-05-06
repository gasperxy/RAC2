#  <span style="color: red">Vaje 5: Usmerjeni grafi</span> 

**Ime:** Hana Lukež

**Datum:** 15.3.2023

---

## <span style="color: red">Naloga 1</span> 

### __Navodilo__
_Imamo graf usmerjen G=(V,E)
 z uteženimi povezavami. Torej imamo neko funkcijo ω:E→A
, ki vsaki povezavi dodeli utež iz množice A.
Navedi nekaj možnih podatkovnih struktur za predstavitev grafa G. Navedi nekaj prednosti oz. slabosti vsake izmed njih. Ponovi tudi, kaj je v grafu pot, sprehod in cikel._


### __Reševanje__
1. Možnosti za predstavitev grafa:
- seznam seznamov: z matriko sosednosti oz. seznamom seznamov lahko predstavimo usmerjeni graf, kjer (i,j)-ti element predstavlja utež na povezavi od i-tega do j-te vozlišča. Neskončna utež na (i,j)-tem mestu pomeni, da povezava iz i-tega v j-to vozlišče ne obstaja. Slabost te podatkovne strukture je, da zavzame veliko prostora, tj. n^2, kjer je n število vozlišč v usmerjenem grafu.



                        
                 A [ i ] [ j ]   = {w(i,j), če (i,j) ∈ E; None, sicer}


Kjer A predstavlja matriko sosednosti, w predstavlja utež.


- seznam sosednosti: v primeru, kadar imamo redek graf. Dobimo vektor z veliko None. 
- slovar sosednosti: G je seznam slovarjev dolžine n.

            G [ i ] = { j : w(i,j) za vska j, da je (i,j) povezava}
G[i]... opisuje okolico i-tega vozlišča


Podatkovne strukture| Prostorska zahtevnost | i in j od soseda ? | sosedi od i
---|---|---|---
Seznam seznamov |  O(n^2) | O(1) | O(n)
Seznam sosednosti | O(n + m) | O(n) | O(1)
Seznam slovarjev | O(n + m) | O(1) | O(n) / O(1)



__Pojmi:__

- Cikel je pot, ki se začne in konča v istem vozlišči, ter gre še čez vsaj eno vozlišče.
- Pot je zaporedje vozlišč v grafu, ki so med seboj povezani z povezavami.
- Sprehod je zaporedje vozlišč v grafu, ki so med seboj povezani z povezavami, vendar za razliko od poti,
se lahko v sprehodu eno vozlišče oz. povezava ponovita večkrat.



## <span style="color: red">Naloga 2</span> 

### __Navodilo__
_Usmerjenemu grafu G z n vozlišči, ki nima ciklov rečemu tudi DAG (directed acyclic graph). Vozlišča takega grafa lahko topološko uredimo. To pomeni, da obstaja da zaporedje vozlišč (v1,v2,…,vn), tako da ne obstaja povezava od vi do vj, če je j<i.
Sestavi algoritem, ki najde tako zaporedje. Namig: Katera vozlišča lahko zagotovo damo na prvo mesto v to ureditev?_

### __Reševanje__

Torej iščemo topološko ureditev grafa, kar pomeni, da če točke narišemo v vrstico morajo vse povezave kazati v desno.

__IDEJA__
- za vhodni podatek imamo matriko sosednjosti, ki predstavlja usmerjenega acikličnega grafa G
- ustvarimo seznam, kamor bomo shranjevali vsa vozlišča, katera nimajo nobene vhodne povezave
_(Izrek: vsak DAG ima vsaj eno vozlišče z vhodno stopnjo)_ [1]
- na vsakem koraku dodamo vsa vozlišča, ki nimajo nobene vstopne povezave, v seznam, nato pa ta vozlišča 
odstranimo iz grafa G, ter vse sosednje povezave
- ta korak ponavljamo tako dolgo, dokler ne izpraznimo grafa G
- za izhodni podatek dobimo seznam vozlišč urejenih topološko


__ČASOVNA ZAHTEVNOST__

O(n+m) + O(n) + O(n+m) = O(n+m), kjer je n število vozlišč in m število povezav

__PYTHON IMPLEMENTACIJA__

```py
def top_sort(G):
    '''Funkcija, ki sprejme graf G, predstavljen z seznamom seznamov, vrne pa topološko ureditev grafa.'''
    n = len(G)   # število vozlišč
    in_deg = [0] * n # in_deg[i] je število povezav, ki kažejo v i
    # gremo čez vsa vozlišča
    for i in range(n):
        # gremo čez vse sosede
        for j in G[i]:
            # obstaja povezava od i-j
            in_deg[j] += 1
    izvori = [i for i in range(n) if in_deg[i] == 0]
    rezultat = []
    
    # dokler bomo imeli vsaj en izvor ponavljamo algoritem
    while izvori:
        izvor = izvori.pop()
        # vsem sosedom izvora odstr. in_deg - 1
        rezultat.append(izvor)
        # gremo čez vse sosede
        for sosed in G[izvor]:
            in_deg[sosed] -= 1
            if in_deg[sosed] == 0:
                # postane nov izvor
                izvori.append(sosed)
    return rezultat

```
Za primer grafa G, ki je prikazan spodaj na sliki, funkcija vrne naslednjo rešitev.



![naloga3_graf_fw.PNG](/Datoteke/1_primer1.png)

```py 
>>> vhod = [[1,2],[3,5],[1,3],[5],[1],[]]
[4, 0, 2, 1, 3, 5]

```
Iz slike spodaj opazimo, da funkcija vrne pravilno rešitev. Opazimo, da sta vozlišče 0 in 4 na obratnem mestu, kot pa v izhodu funkcije. To je vseeno, saj nobeno od teh vozlišč nima nobene vhodne povezave. Vidimo, da so vse puščice obrnjene v desno.

![naloga3_graf_fw.PNG](/Datoteke/1_primer2.png)



## <span style="color: red">Naloga 3</span> 

### __Navodilo__
_Naj bo sedaj G usmerjen utežen graf brez ciklov. Kako bi izračunal ceno najdaljše poti v tem grafu med vozliščema s in t._
### __Reševanje__
__IDEJA__
- pomagamo si s topološko ureditvijo in z dinamičnim programiranjem
- naj bo G usmerjen acikličen graf z utežmi
- naj bo:

        D [i] = najdaljša pot od i do t
        D [t] = 0; smo že v točki t
        D [i] = -inf; začetne vrednosti v začetnem seznamu

        Bellmanova enačba: D [i] = max {D [j] + w}
                             (j,w) ∈ G[i]

        - torej pogledamo vse sosede od i-ja in in izberemo povezavo z največjo utežjo

Če je t nekje na sredini topološke ureditve nas zanimajo samo njegovi predhodniki, na desni strani ostanejo vsi na -inf.

## <span style="color: red">Naloga 4</span> 

### __Navodilo__
_Naj bo G usmerjen utežen graf, kjer je množica uteži enaka {1,2,3}. Kako bi izračunal najcenejšo pot med danima vozliščema u in v. Namig: spomni se kaj počne BFS algoritem._



### __Reševanje__
Algoritem za pregled v širino (ang. Breadth First Search) se uporablja za iskanje najkrajših poti v grafih in sicer s pristopom, da začnemo v korenu drevesa oz. grafa in v naslednjem koraku izberemo povezavo do vozlišča, ki je najbližja prvotnemu. Ta postopek ponavljamo, dokler ne obiščemo vseh vozlišč v grafu.




___
___


#  <span style="color: red">Vaje 6: Floyd-Warshallow algoritem</span> 

**Ime:** Hana Lukež

**Datum:** 22.3.2023

---

## <span style="color: red">Naloga 1</span> 

### __Navodilo__

_Ponovi BFS algoritem. Modificiraj ga, tako da bo iskal najkrajše poti v neuteženem grafu._

### __Reševanje__

BFS oz. Breadth first-search je algoritem, ki ga uporabljamo za iskanje najkrajše poti med vozlišči. Postopek iskanja je takšen, da začnemo v enem vozlišču s in pogledamo vse njegove sosede, nato sosede soseda itd. Uporabljamo ga za iskanje najkrajše poti v neuteženem grafu, za preverjanje dvodelnosti grafa ( z enim sprehodom), za iskanje vpetega drevesa/gozda v grafu, povezanih komponent, za pregled grafa...

DFS oz. Deapth first-search je algoritem, ki začne v nekem vozlišču s, nato pa gre v z iskanjem v globino, dokler ne pride do iskanega vozlišča oz. do konca grafa. Za razliko od BFS, ki najprej pregleda vsa sosednja vozlišča prvotnega s, DFS najprej pregleda vsa sosednja vozlišča v eni smeri.












## <span style="color: red">Naloga 2</span> 

### __Navodilo__
_Ponovi Floyd-Warshallow algoritem. Kaj računa in kaj vrne? Kakšna je njegova časovna zahtevnost?_

### __Reševanje__

Floyd-Warshallov algoritem je primer dinamičnega programiranja, saj temelji na pravilu optimalnosti. Je algoritem za iskanje najkrajših poti v uteženem grafu s pozitivnimi ali negativnimi utežmi. Iščemo najcenejše poti med vsemi pari vozlišč v uteženem grafu-
Nimamo ciklov z negativno ceno.

VHOD: utežen usmerjen graf G z vozlišči v1, ..., vn

IZHOD: matrika D (dij predstavlja ceno najkrajše poti od i do j

dij (k)...cena najkrajše poti od vozlišča vi do vozlišča vj, če so dovoljena vmesna vozlišča v1,v2,...,vk (lahko obiščemo vsa ta vozlišča, kar ne pomeni, da je obvezno)

CILJ: izračunati dij(n) --> n je število vseh vozlišč v grafu

BELLMANOVA ENAČBA:

dij (k) = min {dij(k-1), dik(k-1) + dkj(k-1)}

ROBNI POGOJI:

Dii(1) = 0

D1i(1) = w1i (utež povezave)

ČASOVNA ZAHTEVNOST:
Potrebno je izračunati n matrik velikosti nxn, kar pomeni 
O(n^3) časovno zahtevnost.

PROSTORSKA ZAHTEVNOST: 
Potrebujemo eno matriko, v kateri na vsakem koraku k spreminjamo cene, torej potrebujemo O(n^2) prostora.



## <span style="color: red">Naloga 3</span> 

### __Navodilo__

_Simuliraj FW algoritem na spodnjem grafu._

![naloga3_graf_fw.PNG](/Datoteke/naloga3_graf_fw.PNG)

_Nato dodamo vozlišče 10 in povezavo (5 -> 10) z utežjo -1 in (10 -> 6) z utežjo 2. Kako uporabil prejšnje rezultate, da bi izračunal nove najkrajše poti?_


### __Reševanje__

Za poenostavitev reševanja naloge, sem oznake za vozlišča od 5 do 9 zamenjala z oznakami od 1 do 5.

v5 = v1

v6 = v2

v7 = v3 

v8 = v4

v9 = v5

__k = 0__ (matrika sosednosti)

_|v1 | v2 | v3 | v4 | v5 |
---|---|---|---|---|---|
v1| 0 | 2 | inf | 8 | inf
v2 | inf | 0 | 1 | inf | inf |
v3 | inf | inf | 0 | 2 | inf |
v4 | inf | -2 | inf | 0 | 2 |
v5 | 1 | 7 | -3 | inf | 0 |


__k = 1__

_|v1 | v2 | v3 | v4 | v5 |
---|---|---|---|---|---|
v1| 0 | 2 | inf | 8 | inf
v2 | inf | 0 | 1 | inf | inf |
v3 | inf | inf | 0 | 2 | inf |
v4 | inf | -2 | inf | 0 | 2 |
v5 | 1 | <span style="color: blue">3</span>  | -3 | <span style="color: blue">9</span> | 0 |

__k = 2__

_|v1 | v2 | v3 | v4 | v5 |
---|---|---|---|---|---|
v1| 0 | 2 | <span style="color: blue">3</span> | 8 | inf
v2 | inf | 0 | 1 | inf | inf |
v3 | inf | inf | 0 | 2 | inf |
v4 | inf | -2 | <span style="color: blue">-1</span> | 0 | 2 |
v5 | 1 | 3  | -3 | 9 | 0 |

__k = 3__

_|v1 | v2 | v3 | v4 | v5 |
---|---|---|---|---|---|
v1| 0 | 2 | 3 | <span style="color: blue">5</span> | inf
v2 | inf | 0 | 1 | <span style="color: blue">3</span> | inf |
v3 | inf | inf | 0 | 2 | inf |
v4 | inf | -2 | -1 | 0 | 2 |
v5 | 1 | 3  | -3 | <span style="color: blue">-1</span> | 0 |

__k = 4__

_|v1 | v2 | v3 | v4 | v5 |
---|---|---|---|---|---|
v1| 0 | 2 | 3 | 5 | <span style="color: blue">7</span>
v2 | inf | 0 | 1 | 3 | <span style="color: blue">5</span> |
v3 | inf | <span style="color: blue">0</span> | 0 | 2 | <span style="color: blue">4</span> |
v4 | inf | -2 | -1 | 0 | 2 |
v5 | 1 | <span style="color: blue">-3</span>  | -3 | -1 | 0 |

__k = 5__

_|v1 | v2 | v3 | v4 | v5 |
---|---|---|---|---|---|
v1| 0 | 2 | 3 | 5 | 7
v2 | <span style="color: blue">6</span> | 0 | 1 | 3 | 5 |
v3 | <span style="color: blue">5</span> | 0 | 0 | 2 | 4 |
v4 | <span style="color: blue">-3</span> | -2 | -1 | 0 | 2 |
v5 | 1 | -3  | -3 | -1 | 0 |



Če bi želeli dodati še eno vozlišče v naš graf, bi bilo potrebno dodati v matriko še en stolpec in eno vrstico in podatke izračunati. Na koncu bi izračunali še matriko za k = 6. 


## <span style="color: red">Naloga 4</span> 

### __Navodilo__
_Na predavanjih ste poleg izračuna matrike D(n) izračunali tudi P(n). Kaj lahko iz njih razberemo? Kako dobimo najkrajšo pot med i in j?_

### __Reševanje__

Matrika P(n) nam pove skozi katera vozlišča imamo najkrajši pot od i-tega do j-tega vozlišča.


Za reševanje najkrajše poti sem vzela kar graf iz 2. naloge.

V matriko P(0) bomo vstavljali:
- "-" , če iz iz vozlišča i do j povezava ne obstaja
- v prvi vrstici bomo vstavili 1, če povezava iz vozlišča 1 do j obstaja
- v drugi vrstici bomo vstavili 2, če povezava iz vozlišča 2 do j obstaja
- v tretji vrstici bomo vstavili 3, če povezava iz vozlišča 3 do j obstaja
- v četrti vrstici bomo vstavili 4, če povezava iz vozlišča 4 do j obstaja
- v peti vrstici bomo vstavili 5, če povezava iz vozlišča 5 do j obstaja

P(0) 

_|v1 | v2 | v3 | v4 | v5 |
---|---|---|---|---|---|
v1| - | 1 | - | 1 | -
v2 | - | - | 2 | - | - |
v3 | - | - | - | 3 | - |
v4 | - | 4 | - | - | 4 |
v5 | 5 | 5 | 5 | - | - |

Sedaj moramo izračunati P(1). Pomagamo si iz matrike D(1) iz prejšnje naloge. Pogledamo katera cena se je spremenila v matriki D(1) in na tisto mesto napišemo 1 (v matriko P(1)) saj to pomeni, da če gremo skozi vozlišče 1 je cena poti cenejša.

P(1) 

_|v1 | v2 | v3 | v4 | v5 |
---|---|---|---|---|---|
v1| - | 1 | - | 1 | -
v2 | - | - | 2 | - | - |
v3 | - | - | - | 3 | - |
v4 | - | 4 | - | - | 4 |
v5 | 5 | <span style="color: blue">1</span> | 5 | <span style="color: blue">1</span> | - |


Enako nadaljujemo za :
- P(2) --> tam kjer se je cena poti zmanjšala v D(2), spremenino v P(2) na vozlišče 2
- P(3) --> tam kjer se je cena poti zmanjšala v D(3), spremenino v P(3) na vozlišče 3
- P(4) --> tam kjer se je cena poti zmanjšala v D(4), spremenino v P(4) na vozlišče 4
- P(5) --> tam kjer se je cena poti zmanjšala v D(5), spremenino v P(5) na vozlišče 5





P(2) 

_|v1 | v2 | v3 | v4 | v5 |
---|---|---|---|---|---|
v1| - | 1 | <span style="color: blue">2</span> | 1 | -
v2 | - | - | 2 | - | - |
v3 | - | - | - | 3 | - |
v4 | - | 4 | <span style="color: blue">2</span> | - | 4 |
v5 | 5 | 1 | 5 | 1 | - |

P(3) 

_|v1 | v2 | v3 | v4 | v5 |
---|---|---|---|---|---|
v1| - | 1 | 2 | <span style="color: blue">3</span> | -
v2 | - | - | 2 | <span style="color: blue">3</span> | - |
v3 | - | - | - | 3 | - |
v4 | - | 4 | 2 | - | 4 |
v5 | 5 | 1 | 5 | <span style="color: blue">3</span> | - |

P(4) 

_|v1 | v2 | v3 | v4 | v5 |
---|---|---|---|---|---|
v1| - | 1 | 2 | 3 | <span style="color: blue">4</span>
v2 | - | - | 2 | 3 | <span style="color: blue">4</span> |
v3 | - | <span style="color: blue">4</span> | - | 3 | <span style="color: blue">4</span> |
v4 | - | 4 | 2 | - | 4 |
v5 | 5 | <span style="color: blue">4</span> | 5 | 3 | - |

P(5) 

_|v1 | v2 | v3 | v4 | v5 |
---|---|---|---|---|---|
v1| - | 1 | 2 | 3 | 4
v2 | <span style="color: blue">5</span> | - | 2 | 3 | 4 |
v3 | <span style="color: blue">5</span> | 4 | - | 3 | 4 |
v4 | <span style="color: blue">5</span> | 4 | 2 | - | 4 |
v5 | 5 | 4 | 5 | 3 | - |


Sedaj, ko imamo izračunano matriko P(5), lahko povemo za vsak par vozlišč, pot po kateri je cena najmanjša.
Naprimer:
- želeli bi priti iz v4 v v2. Pogledamo vrednost na mestu P43(5) = 2, kar pomeni, da če želimo priti najceneje iz v4 v v3, mnoramo prečkati v2. Če pogledamo v matriko D, na mesto D43(5) = -1. Če preverimo to na grafu vidimo, da je res potrebno prečkati vozlišče v2 in da je cena te poti enaka -1.


## <span style="color: red">Naloga 5</span> 

### __Navodilo__
_Kako bi s FW algoritmom odkrili, če v grafu obstajajo negativni cikli? Kaj vrne FW, če graf vsebuje negativen cikel?_
### __Reševanje__
Ali ima graf kakšen negativen cikel lahko preverimo tako, da pogledamo elemente na diagonali končne matrike. Če je kakšen element negativen, potem ima graf negativen cikel.

__NEGATIVEN CIKEL__ v grafu je cikel, kjer je vsota povezav negativna.
___
___
#  <span style="color: red">Vaje 7: Floyd-Warshallov algoritem in Dijkstrin algoritem</span> 

**Ime:** Hana Lukež

**Datum:** 28.3.2023

---

## <span style="color: red">Naloga 1</span> 
### __Navodilo__
Iz prejšnjih vaj obravnavaj, kako razberemo najkrajše poti s pomočjo matrike Π
, ki jo dobimo z FW algoritmom.
### __Reševanje__

To nalogo sem že rešila (vaje 6, naloga 4)


## <span style="color: red">Naloga 2</span> 
### __Navodilo__
Uteži sedaj dodamo še na vozlišča. Kako sedaj poiskati najcenejše poti?

### __Reševanje__

To nalogo sem že rešila (vaje 6, naloga 4).



## <span style="color: red">Naloga 4</span> 
### __Navodilo__
Na neki borzi se trgujejo valute po menjalnem tečaju, ki ga podaja tabela R
 velikosti n×n
, kjer je n
 število različnih valut. Vrednost R[i][j]
 pove, da za a
 enot valute i
 dobimo a⋅R[i][j]
 enot valuje j
. Ker menjalni tečaji lahko hitro spreminjajo in so odvisni od raznih parametrov se lahko zgodi, da R[i][j]⋅R[j][i]≠1
.

Za primer si oglejmo naslednjo shemo: 

![7_vaje_naloga4.PNG](/Datoteke/7_vaje_naloga4.png)


Če trgujemo USD -> YEN -> EUR -> USD končamo z 1.44 USD. Tako zaporedje imenujemo arbitraža.

Predpostavi, da ne obstaja arbitražnih zaporedij. Kako bi poiskal najbolj ugodno pretvorbo valute i
 v valuto j
?

Kaj pa če sedaj opustimo predpostavko in dovoljujemo, da arbitražna zaporedja obstajajo. Kako bi odkril, kakšna so?

### __Reševanje__


## <span style="color: red">Naloga 5</span> 
### __Navodilo__
Ponovi Djikstrov algoritem. Kaj so vhodni in izhodni podatki, kakšne so predpostavk, itd.

Zapiši tudi njegovo glavno idejo oziroma kar psevdo kodo.

### __Reševanje__
Podano imamo omrežje G. S pomočjo Dijkstrinega algoritma lahko poiščemo najkrajšo pot od enega vozlišča s do vseh ostalih, ob predpostavki, da so uteži vseh povezav pozitivne. 

__VHOD:__ Utežen usmerjen graf G, predstavljen z seznamom sosednosti in začetno vozlišče s.

__IZHOD:__ Seznam razdalj, ki predstavlja razdalje od vozlišča s do vseh ostalih vozlišč. Vrne tudi seznam poti, ki predstavlja drevo najkrajše poti od vozlišča s do vseh ostalih.

__IDEJA:__
- Na vsakem koraki si zapomnimo dolžino najkrajše poti od začetnega do trenutnega vozlišča in pa zadnjo povezavo na najkrajši poti od začetnega do trenutnega vozlišča.
- Na začetu nastavimo vse vrednosti vozlišč na neskončno, razen začetno vozlišče nastavimo na 0. Dokler ne uredimo vse povezave (dokler ne velja pravilo optimalnosti), popravljamo ustrezne vrednosti. Vrednosti pa popravljamo tako, da vedno izberemo tisto vozlišče izven drevesa, ki bo najmanj oddaljeno od začetnega vozlišča s.

__PSEVDO KODA:__





## <span style="color: red">Naloga 6</span> 

### __Navodilo__
Simuliraj Dijkstrov algoritem na spodnjem grafu.

![7_vaje_naloga4.PNG](/Datoteke/7_vaje_naloga6.png)

### __Reševanje__

Naloge sem se lotila tako, da sem najprej izpisala vse povezave iz grafa G s podanimi utežmi:

- A-B 1
- A-C 3
- B-E 4
- B-C 6
- B-D 1
- C-E 3
- C-D 1
- C-G 6
- E-G 2
- D-G 2
- D-F 6
- G-H 1
- F-H 3
- F-C 2

Nato sem nastavila vse cene vozlišč na inf, razen začetno vozlišče A sem nastavila na 0.
v | razdDo[] | povezDo[]
---|---|---|
A |  0| - |
B | inf | - |
C | inf | - |
D | inf | - |
E | inf | - |
F | inf | - |
G | inf | - |
H | inf | - |


Sedaj pa na vsakem koraku dodajamo vozlišča v drevo in popravljamo vrednosti vozlišč. Vozlišča dodajamo v drevo glede na začetno vozlišče A.

Na prvem koraku pogledamo sosednja vozlišča vozlišča A, torej B in C. Vrednosti povezav dodamo v tabelo, poleg tega si zapomnimo tudi zadnje vozlišče preko katerega smo prišli v to vozlišče, torej A. Postopek nadaljujemo, dokler v grafu ne velja pravilo optimalnosti, torej ne moremo več popraviti nobene cene vozlišča.

VOZLIŠČE A:

v | razdDo[] | povezDo[]
---|---|---|
A | 0 | - |
B | 1 | A-B |
C | 3 | A-C |
D | inf | - |
E | inf | - |
F | inf | - |
G | inf | - |
H | inf | - |




VOZLIŠČE B:

v | razdDo[] | povezDo[]
---|---|---|
A | 0 | - |
B | 1 | A-B |
C | 3 | A-C |
D | 2 | B-D |
E | 5 | B-E |
F | inf | - |
G | inf | - |
H | inf | - |


VOZLIŠČE C:

v | razdDo[] | povezDo[]
---|---|---|
A | 0 | - |
B | 1 | A-B |
C | 3 | A-C |
D | 2 | B-D |
E | 5 | B-E |
F | inf | - |
G | 9 | C-G |
H | inf | - |


VOZLIŠČE D:

v | razdDo[] | povezDo[]
---|---|---|
A | 0 | - |
B | 1 | A-B |
C | 3 | A-C |
D | 2 | B-D |
E | 5 | B-E |
F | 8 | D-F |
G | 4 | D-G |
H | inf | - |

VOZLIŠČE E:

v | razdDo[] | povezDo[]
---|---|---|
A | 0 | - |
B | 1 | A-B |
C | 3 | A-C |
D | 2 | B-D |
E | 5 | B-E |
F | 8 | D-F |
G | 4 | D-G |
H | inf | - |

VOZLIŠČE F:

v | razdDo[] | povezDo[]
---|---|---|
A | 0 | - |
B | 1 | A-B |
C | 3 | A-C |
D | 2 | B-D |
E | 5 | B-E |
F | 8 | D-F |
G | 4 | D-G |
H | 11 | F-H |

VOZLIŠČE G:

v | razdDo[] | povezDo[]
---|---|---|
A | 0 | - |
B | 1 | A-B |
C | 3 | A-C |
D | 2 | B-D |
E | 5 | B-E |
F | 8 | D-F |
G | 4 | D-G |
H | 5 | G-H |

VOZLIŠČE H:

v | razdDo[] | povezDo[]
---|---|---|
A | 0 | - |
B | 1 | A-B |
C | 3 | A-C |
D | 2 | B-D |
E | 5 | B-E |
F | 8 | D-F |
G | 4 | D-G |
H | 5 | G-H |

Zadnja tabela predstavlja cene poti od vozlišča A do vseh ostalih vozlišč ter drevo najkrajših poti do vseh vozlišč.
Drevo najkrajših poti z vrednostmi povezav sem prikazala na spodnji sliki.

![7_vaje_naloga4.PNG](vaje7_naloga6.png)


Svojo rešitev sem preverila tudi v implementirani funkciji dijkstra.py.

```py
>>> G2 = [[(1,1), (2,3)],
      [(4,4),(2,6),(3,1)],
      [(4,3),(3,1),(6,6)],
      [(6,2),(5,6)],[(6,2)],
      [(7,3),(2,2)],[(7,1)],
      []]

>>> print(razdalje)

[0, 1, 3, 2, 5, 8, 4, 5]
```

___
___


#  <span style="color: red">Vaje 8: Dijkstra in BFS</span> 

**Ime:** Hana Lukež

**Datum:** 5.4.2023

---

## <span style="color: red">Naloga 1</span> 

### __Navodilo__
Na naslovu https://unilj-my.sharepoint.com/:f:/g/personal/gasper_romih_fmf_uni-lj_si/EgIVtB_YcP1Cs6MMyjtiFCcBSEEHYH9rzpd63Ll_sXAXrA?e=QMRZzr, 

imate na razpolago dve datoteki:

djikstra.py -> moja implementacija djikstrovega algoritma
roadNet-TX.txt -> datoteka za informacijami o cestnem omrežju v Texasu. Vozlišča so bodisi križišča oz. končne destinacije povezave pa so ceste med temi vozlišči. Povezave oz. ceste niso utežene so pa usmerjene.

Vaša naloga bo, da uporabite ta algoritem na teh podatkih, torej:

roadNet-TX.txt spremenite v ustrezno podatkovno strukturo grafa.
poiščete najkrajše razdalje od vozlišča 100 do vseh ostalih.
Koliko je razdalja dG(100,100000)
 ?
Katero vozlišče je najbolj oddaljeno od vozlišča 100?
Koliko vozlišč je dosegljivih iz vozlišča 100?


### __Reševanje__

dijkstra.py
```py
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

V datoteki roadNet-TX.txt je predstavljen graf G brez uteži, kjer prvi stolpec predstavlja izhodno vozlišče povezave, drugi stolpec pa vhodno vozlišče povezave tj. graf je usmerjen.

Najprej sem naredila funkcijo, ki sprejme ime datoteke in preuredi tekstovno datoteko tako, da vrne seznam naborov izhodnega in vzhodnega vozlišča. Potrebno je bilo preskočiti prve štiri vrstice, saj niso bili podatki, ki jih potrebujemo. Na koncu je bilo potrebno razvrstiti seznam naborov po izhodnem vozlišču povezave, zato da vemo koliko je vseh povezav.

```py
def datoteka(ime):
    '''Funkcija, ki spremeni datoteko txt v seznam parov vozlišč.'''
    seznam = list()
    with open(ime, 'r') as file:
        vse_vrst = file.readlines()
        vrstice = vse_vrst[4:]
        for i in vrstice:
            i = i[:-1]
            od = int(i.split('\t')[0])
            do = int(i.split('\t')[1])
            seznam.append((od, do))
        seznam.sort(key=lambda a: a[0])
    return seznam
```

Nato sem ustvarila funkcijo, ki sprejme seznam parov vozlišč, konstruiran v zgornji funkciji. Vrne pa seznam seznamov sosednjih vozlišč z utežmi povezav 1.
```py
def seznam_sosednosti(seznam):
    '''Funkcija, ki spremeni seznam parov sosednjih vozlišč v seznam sosednosti z utežjo 1.'''
    sez_seznamov = [list() for _ in range(seznam[-1][0] + 1)] # toliko je vseh vozlišč
    for i,j in seznam:
        sez_seznamov[i].append((j,1))
    return sez_seznamov
```

šč je dosegljivih iz vozlišča 100?

a) Poiščete najkrajše razdalje od vozlišča 100 do vseh ostalih.
S pomočjo zgornji funkcij sem tekstovno datoteko pretvorila v obliko, ki jo sprejme datoteka dijkstra.py. Nato pa sem za vozlišče s določila 100, ter tako izračunala vse najkrajše poti od vozlišča 100 do vseh ostalih vozlišč.

```py
primer1 = datoteka("roadNet-TX.txt")
graf = seznam_sosednosti(primer1)
najkrajse_razdalje_od_sto, poti = djikstra(graf, 100)
print(najkrajse_razdalje_od_sto)
```

b) Koliko je razdalja dG(100,100000)?
Funkcija dijkstra.py vrne vrne dva seznama: razdalje do vseh vozlišč in poti. Potrebno je iz seznama razdalj vzeti vrednost za indeks 100000.

```py
dG = najkrajse_razdalje_od_sto[100000]
print(dG)
```
ODGOVOR: 240

c) Katero vozlišče je najbolj oddaljeno od vozlišča 100?
Iz seznama razdalj sem razbrala katera je največja razdalja, nato pa sem s pomočjo funkcije index() poiskala katero je to vozlišče, ki je najbolj oddaljeno od 100.
```py
najvecja_razdalja = max(najkrajse_razdalje_od_sto)
ind = najkrajse_razdalje_od_sto.index(najvecja_razdalja)
print(ind)
```
ODGOVOR: 1389039


d) Koliko vozlišč je dosegljivih iz vozlišča 100?
To so vsa vozlišča, kjer je razdalja v seznamu razdalj večja ali enaka 1.

```py
def koliko_vozlisc(seznam):
    stevec = 0
    for i in seznam:
        if i >= 1:
            stevec += 1
    return stevec

print(koliko_vozlisc(najkrajse_razdalje_od_sto))
```
ODGOVOR: 1351136
    


## <span style="color: red">Naloga 2</span> 

### __Navodilo__

Glede na to, da graf ni utežen, lahko za isto nalogo implementiramo BFS algoritem. Implementiraj BFS algoritem, ki bo poiskal dolžine najkrajših poti od s do vseh ostalih vozlišč. Vrne naj tudi drevo najkrajših poti, tako kot Djikstra. Preveri iste zadeve kot zgoraj, dobiti moraš seveda iste odgovore.

### __Reševanje__

```py
def BFS(G, s):
    '''Funkcija, ki vrne najkrajše poti od vozlišča s do vseh ostalih vozlišč, in tudi drevo najkrajših poti.'''
    n = len(G)
    razdalje = [0]*n
    obiskani = [False]*n
    q = [(s, 0, s)]  # začnemo v u
    poti = [None]*n
    while q:
        trenutni, razdalja, pred = q.pop(0)
        if obiskani[trenutni]:
            continue
        obiskani[trenutni] = True
        razdalje[trenutni] = razdalja
        poti[trenutni] = pred
        for sosed, cena in G[trenutni]:
            if not obiskani[sosed]:
                q.append((sosed, razdalja+1, trenutni))
    return razdalje, poti
```

## <span style="color: red">Naloga 3</span> 

### __Navodilo__
Oba algoritma dodelaj, tako da dodaš nov vhodni podatek t, ki predstavlja končno vozlišče. Algoritma naj torej vrneta razdaljo med s
in t v grafu ter pote (kot drevo) med njima. Delujeta naj, tako da se ustavita takoj ko najdemo željeno pot.
### __Reševanje__

```py
def djikstra_druga(G, s, t):
    '''Funkcija, ki vrne razdaljo med s in t v grafu G ter pot (kot drevo) med njima.'''
    n = len(G)
    obiskani = [False] * n
    razdaljeDo = [-1] * n
    poti = [None] * n
    Q = [(0, s, s)]
    while Q:
        razdalja, u, p = heapq.heappop(Q)  
        if obiskani[u]:
            continue
        obiskani[u] = True
        razdaljeDo[u] = razdalja
        poti[u] = p
        if u == t:
            break
        for (v, teza) in G[u]:
            if not obiskani[v]:
                heapq.heappush(Q, (razdalja + teza, v, u))
    return razdaljeDo, poti
```


```py
def BFS_druga(G, u, t):
        '''Funkcija, ki vrne razdaljo med s in t v grafu G ter pot (kot drevo) med njima.'''
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


## <span style="color: red">Naloga 4</span> 

### __Navodilo__
Zapiši funkcijo, ki sprejme začetno vozlišče s, končno vozlišče t
 ter drevo najkrajših poti ter vrne najkrajšo pot med njima v obliki seznama.

Sedaj rekonstruiraj najkrajšo pot med vozliščem 100 in 100000.

### __Reševanje__

```py
def najkrajša_pot(s, t, drevo_najkrajsih):
    '''
        Funkcija, ki sprejme začetno vozlišče s, končno vozlišče t
        ter drevo najkrajših poti ter vrne najkrajšo pot med njima v obliki seznama.
    '''
    sez = list()
    v = drevo_najkrajsih[t]
    sez.append(t)
    while v != s:
        sez.append(v)
        v = drevo_najkrajsih[v]
    sez.append(s)
    return sez
```


## <span style="color: red">Naloga 5</span> 

### __Navodilo__
Analiziraj časovne zahtevnosti algoritmov. Primerjaj hitrost med djikstro in BFS-jem. Prav tako analiziraj razliko med djikstro, ki izračuna najkrajše poti od s do vseh ostalih ter jo primerjaj z tisto verzijo iz Naloge 3.

Če nas bi zanimale najkrajše poti od s do t_1, t_2, ..., t_k, kateri algoritem bi uporabil? Probaj odgovor podat na podlagi parametra k, ter analize, ki si jo opravil.

### __Reševanje__

![primerjava_casovne_zahtevnosti.PNG](/Datoteke/primerjava_casovne_zahtevnosti.png)

Uporabila bi algoritem BFS, saj je v obeh primerih hitrejši.
___
___


#  <span style="color: red">Vaje 9: Bellman-Fordov algoritem</span> 

**Ime:** Hana Lukež

**Datum:** 11.4.2023

---

## <span style="color: red">Naloga 1</span> 

### __Navodilo__
Konstruirajte nov graf, ki vsebuje le vozlišča od 0 do N.

Vsaki povezavi določite neko pozitivno utež (lahko čisto naključno) in zadevo shranite v novo .txt datoteko. Vrstice naj bodo oblike u v w(u,v), kjer je (u,v) povezava in w(u,v) njena utež.

### __Reševanje__
Opomba: Kodo sem si sposodila od sošolke Diane Škof.

```py
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
                        



## <span style="color: red">Naloga 2</span> 
### __Navodilo__
Implementiranje še Bellman-Fordov algoritem in ga poženite na grafu iz prejšnje naloge. Analiziraje kako velik N iz prejšne naloge morate vzeti, da bo algoritem še deloval v zglednem času.

### __Reševanje__

Opomba: Kodo sem si sposodila od sošolke Diane Škof.

```py
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


___
___


#  <span style="color: red">Vaje 10: Kopica</span> 

**Ime:** Hana Lukež

**Datum:** 19.4.2023

---

__PREDSTAVITEV KOPICE__
- kopica je drevesna podatkovna struktura (ne nujno dvojiško drevo)
- mi se bomo osredotočili na dvojiško kopico, ki jo predstavimo z dvojiškim drevesom
- lastnosti: kopična lastnost (za poljubni vozlišči oče in sin, velja enaka relacija R med tema vozliščema tj. oče R sin); leva poravnanost (smiselno uporabiti v tabeli)

## <span style="color: red">Naloga 1</span> 

### __Navodilo__
Simuliraj delovanje (min) kopice. Za vsavljanje je kot operacija število, za brisanje pa x. Za boljšo predstavo nariši kar drevesa.

Operacije: 8,2,1,3,7,6, x, x, 5, x, -3, x

### __Reševanje__

![1_kopica.PNG](/Datoteke/1_kopica.png)
![2_kopica.PNG](/Datoteke/2_kopica.png)
![3_kopica.PNG](/Datoteke/3_kopica.png)
![4_kopica.PNG](/Datoteke/4_kopica.png)

                    
## <span style="color: red">Naloga 2</span> 
### __Navodilo__
Predstavi kopico s seznamom in zapiši delovanje pop() in push(x) operacij.
### __Reševanje__
Za kopico mora veljati leva poravnanost, da jo lažje predstavimo s seznamom. Namreč, če za kopico ne bi veljala leva poravnanost, bi v tabeli imeli ogromno nepotrebnih polj z vrednostmi None ali 0. Tako pa dejansko uporabimo ves prostor.

$T$...kopica predstavljena s seznamom dolžine $n$

$T[i]$... $i$-ti element seznama oz. $i$-to vozlišče

Pri predstavitvi kopice s seznamom, za prvi element vzamemo kar 0, zaradi lepšega zapisa enačb.
Torej prvi element (koren drevesa) postavimo na mesto i=1 v seznam. V tem primeru imamo očeta od vozlišča $i$ na mestu $i // 2$, levi sin od vozlišča $i$ je na mestu $2i$, ter desni sin na mestu $2i + 1$.

Če pa koren drevesa postavimo na mesto i=0 v seznamu pa dobimo naslednje formule:
- oče od $i$ --> na mestu $(i-1)//2$
- levi sin od $i$ --> na mestu $2i + 1$
- desni sin od $i$ --> na mestu $2i + 2$ 

```py
def push(k, x):
    '''Funkcija, ki doda element x v kopico k in preuredi nov seznam z dodanim vozlišče, da ima lastnosti kopice.'''
    # primer za minimalno kopico
    k.append(x)
    i = len(k) - 1 #indeks od x
    oce = i // 2
    while k[i] < k[oce]:
        T[i], T[oce] = T[oce], T[i]
        i = oce
        oce = i//2


```

```py
def pop(k):
    '''Funkcija, ki iz seznama odstrani koren kopice k (najmanjši element, saj delamo za minimalno kopico), in preuredi seznam, da spet postane kopica.'''
koren = k[1]
n = len(k) 
zadnji_el = k[n-1]
koren = zadnji_el #koren postavimo za list drvesa
k.pop() # ta funkcija izbriše zadnji element iz kopice
i = 1 # novi koren se nahaja na mesti i=1
levi_s = 2 * i
desni_s = 2 * i + 1
while k[i] > k[levi_s] or k[i] > k[desni_s]:
    if k[levi_s] < k[desni_s]:  # če je levi sin manjši od desnega, potem očeta zamenjamo z levim sinom
        k[i], k[levi_s] = k[levi_s], k[i]
        i = levi_s
        levi_s = 2*i
        desni_s = 2*i + 1
    else:
        k[i], k[desni_s] = k[desni_s], k[i]
        i = desni_s
        levi_s = 2*i
        desni_s = 2*i + 1
return koren

```



## <span style="color: red">Naloga 3</span> 

### __Navodilo__
Kako bi s kopico sortiral seznam? Časovna zahtevnost? Kako in podanega seznama nardiš kopico v O(n) časa.

### __Reševanje__

- Najprej imamo podan seznam elementov, ki so neurejeni. Najprej jih uredimo v kopico. Če želimo na koncu imeti podatke urejene od najmanjšega do največjega, jih v kopico dodajamo v obratnem vrstnem redu. Seznam imamo razdeljen na dva dela: levi neurejen in desni urejen. Na začetku so vsi elementi v neurejenem delu. Ko imamo kopico, na vsakem koraku izločamo koren drevesa oz. ga postavimo na konec seznama, ki je urejen. Na vsakem koraku preuredimo drevo, da je kopica in postopek nadaljujemo. Na koncu dobimo urejen seznam elementov.


- Gradnja kopice in vstavljanje najmanjšega elementa je časovne zahtevnosti  $O(n) $, kjer je  $n$ število elementov v tabeli. Veliko več nas stane popravljanje kopice na vsakem koraku tj.  $O(n * logn) $. Torej skupa je časovna zahtevnost $O(n * logn)$.

- Denimo, da imamo levo poravnano drevo, katerega koren je K. Predpostavimo, da sta levo in desno drevo K-ja že kopici in da je K koren drevesa. Torej, ker sta L in D že kopici, je edino kar moramo še storiti to, da koren prestavimo po drevesu navzdol na pravilno višino drevesa.
V tem primeru imamo dve možnosti:
1.	K ima večjo ali enako vrednost kot njegova otroka, kar pomeni, da je konstrukcija zaključena, kot v naslednjem primeru.
2.	K ima vrednost manjšo od enega ali celo obeh od sinov: V tem primeru bi moral K biti zamenjan z sinom, ki ima večjo vrednost. Rezultat bo sedaj kopica, razen v primeru, če je K še vedno manjši od vrednosti drugega otroka ali pa celo obeh. V tem primeru enostavno nadaljujemo s pomikanjem K-ja navzdol po drevesu, dokler ne doseže višine kjer je večji od svojega sina ali pa postane list.

Na takšen način lahko konstruiramo že podan seznam v kopico v $O(n)$ časa.
___
___





















# Viri
 [1] https://ucilnica.fri.uni-lj.si/pluginfile.php/133254/mod_resource/content/0/F1-GrafiAlg.pdfž


















