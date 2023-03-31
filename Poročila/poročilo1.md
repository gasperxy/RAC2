# Poročilo za vaje
**Ime:** Zala Duh

## Vsebina
* Vaje 1 (15.2.2023)
* Vaje 2 (22.2.2023)
* Vaje 3 (1.3.2023)
* Vaje 4 (8.3.2023)

# Vaje 1
**Datum**: 15.2.2023


Na vajah smo se ukvarjali z negaterimi osnovnimi podatkovnimi strukturami v pythonu in njihovimi časovnimi zahtevnostimi. Nato pa smo rešili še naloge v Tomu.

___________________
### **1. naloga**
Za podatkovne strukture v pythonu seznam, slovar in verižni seznam zapiši njihove časovne zahtevnosti za:

- dodajanje na začetku/sredini/koncu
- poizvedbe
- iskanje
- brisanje začetku/sredini/koncu

![Alt text](/Datoteke/vaje1.jpg)
_________________
### **2. naloga**

**Opis:**

Žabica se je izgubila v močvari in želi kar se da hitro odskakljati ven. Na srečo močvara vsebuje veliko muh, s katerimi si lahko povrne energijo, kajti utrujena žabica ne skoči daleč.

S funkcijo zabica(mocvara) želimo ugotoviti, kako hitro lahko žabica odskaklja iz močvare. Močvaro predstavimo s tabelo, kjer žabica prične na ničtem polju. Če je močvara dolžine k, je cilj žabice priskakljati vsaj na k-to polje ali dlje (torej prvo polje, ki ni več vsebovano v tabeli).

Energičnost žabice predstavimo z dolžino najdaljšega možnega skoka. Torej lahko žabica z količino energije e skoči naprej za katerokoli razdaljo med 1 in e, in če skoči naprej za k mest ima sedaj zgolj e - k energije. Na vsakem polju močvare prav tako označimo, koliko energije si žabica povrne, ko pristane na polju. Tako se včasih žabici splača skočiti manj daleč, da pristane na polju z več muhami. Predpostavimo, da ima vsako polje vrednost vsaj 1, da lahko žabica v vsakem primeru skoči naprej.

V primeru [2, 4, 1, 2, 1, 3, 1, 1, 5] lahko žabica odskaklja iz močvare v treh skokih, v močvari [4, 1, 8, 2, 11, 1, 1, 1, 1, 1] pa potrebuje zgolj dva.


 Nalogo rešimo s pomočjo dinamičnega programiranja in to tako, da najprej problem razdelimo na več manjših podproblemov, ki se med seboj pokrivajo.


**muhe[i]** = število muh na i-tem lokvanju

**žabica(i, e)** (kjer $e$ predstavlja energijo, $i$ pa polje, kjer se žabica nahaja) = minimalno število skokov, tako da pridemo ven iz močvare, če se nahajamo na $i$-tem mestu z $e$ energije

Bellamova enačba za naš problem:

![Alt text](/Datoteke/bellmanova_enacba_zabica.png)

Koda z memoizacijo:

```python
def zabica(mocvara):
    def skaci(i,e):
        if i >= len(mocvara):
            return 0
        if (i,e) in memo:
            return memo[(i,e)]
        nova_energija = e + mocvara[i]
        min_skokov = min(skaci(i+k, nova_energija - k) for k in range(1, nova_energija +1))
        memo[(i,e)] = 1+ min_skokov
        return memo[(i,e)]
    memo = {}
    return skaci(0,0)
```

Koda s pomočjo iteracije: (kodo sem si sposodila od sošolca Adnana Pajalića)
```python 
def zabica_iterativno(mocvara):
    """Iterativni postopek za iskanje najmanjšega števila skokov"""
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
**Ocenili smo tudi časovno zahtevnost:**


- *iterativna metoda:*  
  Izračunati moramo vsa stanja: $$ O(n^2) \times O(n) = O(n^3)$$
    $O(n^2)$ -> število stanj

    $O(n)$ -> čas za izračun enega stanja


**Primerjava časovne zahtevnosti:**
Z roza barvo je žabica iterativno, z vijolično pa žabica z memoizacijo.
![Alt text](/Datoteke/Figure_1.png)

# Vaje 2
**Datum**: 22.2.2023

Na 2. vajah smo ponovili 0/1 nahrbtnik in rešili smo dve nalogi. Prva je bila malo daljša in je vsebovala S in Z množice. Druga pa je bila malo krajša. 
___________

### Komentarji in opombe 
Vaje so se mi zdele zanimive in všeč mi je bilo, da smo naloge rešili skupaj in počasi tako, da smo jih vsi razumeli. 
______
### **1. naloga**
Skupaj smo na tablo reševali nasledjo nalogo:

![Alt text](/Datoteke/vaje2_naloga1.png)



Odgovorili smo na naslednja vprašanja:

1. **Pri prepisu množice Z5 je pri natanko enem paru prišlo do napake. Kateri par je napačen in
kakšen bi moral biti? Opiši, kako lahko napako ugotovimo, ne da bi šli Z5 računati na novo.**

Napačen je  5-ti predmet (45,6). Moral bi biti:

Z5 = S4 ++ (45,6)

Z5 = [(45,6), (56,12), **(72,16)**,...]

Zgoraj zadnji člen je pravilen namesto (72,20).

Brez računanja Z5 bi lahko napako ugotovili tudi tako, da bi preverili, če je Z5 naraščujoča.

2. **Če imamo na voljo 160 enot prostora, kakšna je optimalna vrednost nahrbtnika?**

V S8 pogledamo zadnji manjši par (w,c) tako, da je W <= 160. Tak par je (153,40). Iz tega sledi, da je optimalna vrednost 40.

3. **Koliko neizkoriščenega prostora nam ostane, če optimalno napolnimo nahrbtnik velikosti 110 s prvimi petimi predmeti. Kakšna je ta optimalna vrednost polnitve? Opiši vse možne načine, kako dosežemo to optimalno vrednost!**

Gledati moramo S5 - ker nas zanima samo prvih pet predmetov. W = 110 in i = 5.

 Optimalna vrednost polnitve je 26. Izberemo is par (99,26) in tako nam ostan 11 enot neizkoriščenega prostora.

![Alt text](/Datoteke/vaje2_1.jpg)


4. **Skiciraj graf funkcije, ki pokaže, kako se v odvisnosti od razpoložljivega prostora spreminja optimalna vrednost nahrbtnika, če imamo na voljo prvih 6 predmetov in 6. predmet moramo dati v nahrbtnik.**
Opazujemo Z6, ker 6.element vzamemo. 
![Alt text](/Datoteke/vaje2.jpg)

5. **Ugotovili smo, da imamo na voljo še en predmet, in sicer velikosti 15 in vrednosti 4 (torej je na voljo 9 predmetov). Kakšna je optimalna vrednost nahrbtnika, ki ima 180 enot prostora? Opiši vse možne načine, kako dosežemo to optimalno vrednost!**

Naloge se lahko lotimo na dva načina:

**1.način**:
 
Izračunamo množico Z9 na roke.

 $Z9 = S8 ++ (15,4) = [(15,4), (24,9), (26, 10), (35,15), (61,19),...]$

 $S9 = S8 U Z9$ (max. zlitje)

Za S9 razberemo rezultat.

**2.način**:

Pomagamo si z Bellamnovo enačbo:
$G(9,180) = max(G(8,180), g(9, 165) + 4) $

Tako iz S8 razberemo: 


- $G(8, 180) = 40$
- $G(8,165) + 4 = 44 $
>
In tako dobimo, da je optimalna vrednosr nahrbtnika z 180 enot prostora 44.
>
![Alt text](/Datoteke/vaje2_2.jpg)
______

### **2. naloga** 

Rešimo na tablo naslednji problem. Na voljo imamo seznam pozitivnih naravnih števil sez in naravno število S.

Zanima nas, ali lahko S zapišemo kot vsoto števil iz sez. 

Recimo: sez = [3, 34, 4, 12, 5, 2], S = 9 vrne True, saj 9 = 4 + 5.

Zapiši dinamični problem (Bellmanovo enačbo) ter oceni časovno zahtevnost.




Zapis Bellmanove enačbe:

![Alt text](/Datoteke/bellmanova_enacba2.png)
Prva možnost je da vzamemo i-ti element, druga pa da ga ne vzamemo. Vmes je *or* ker nam je vseeno kdaj dosežemo vsoto.

Robni primeri, ki nastopijo:
- $vsota(0,0) = True$
- $vsota(i,0) = False$



# VAJE 3
**Datum**: 1.3.2023

Na vajah smo izvedli tekmovanje v parih. Reševali smo naloge na Tomo-tu iz poglavja *Tekomovanje - nahrbtnik*.  V paru sem bila skupaj z Mužič Anejem.

### Komentarji in opombe
Vaje so mi bile zanimive, ker so bile drugačne kot običajno. Všeč mi je bilo delo v parih, saj smo skupaj si skupaj s sošolci lahko delili znanje in tako lažje in hitreje prišli do rešitve.

###  **1. naloga**
Opis:

Implementiraj funkcijo optimalni_tovor(predmeti, W), ki vrne največjo skupno ceno predmetov, ki jih lahko trgovec natovori na letalo z maksimalno nosilnostjo W. 

Koda:
```python
from functools import lru_cache
def optimalni_tovor(predmeti,w):
    '''Funkcija vrne največjo skupno ceno predmetov, ki jih lahko trgovec natovori na letalo z max. nosilnostjo w'''
    n = len(predmeti)
    @lru_cache(maxsize=None)
    def memo(i,W):
        if W<0: #primer ko letala nimamo
            return float('-inf')
        if i == 0 or W == 0: #primer če nimamo prostora in nimamo niti predmetov
            return 0
        #i-ti predmet ali vzamemo ali pa ne
        neVzamemo = memo(i-1,W)
        vzamemo = memo(i-1, W-predmeti[i-1][1]) + predmeti[i-1][0]

        return max(vzamemo, neVzamemo)
    return memo(n,w)
```
Primeri:
```python
>>> predmeti = [(4,6),(5,2),(6,10),(7,3),(10,4)]
>>> w = 15
>>> optimalni_tovor(predmeti,w)
26
>>> predmeti = [(40,4353), (45,3224), (34,768), (12,799),(4,654),(87,999)]
>>> w = 10000
>>> optimalni_tovor(predmeti,w)
210
>>> predmeti = [(19, 6309), (73, 6807), (30, 2201), (22, 9218), (77, 6274), (68, 4114), (27, 7668), (54, 3871), (49, 5739), (55, 1298), (89, 7515), (20, 3797)]
>>> w = 100000
>>> optimalni_tovor(predmeti,w)
583
```

### **2. naloga**
Opis:

Implementiraj funkcijo optimalni_predmeti(predmeti, W), ki vrne seznam predmetov ki dosežejo največjo vrednost, če lahko na letalo natovorimo skupno težo največ W. Če je možnosti več, vrni katerokoli.

Koda:
```python
def optimalni_predmeti(predmeti, W):
    '''Vrne seznam predmetov, ki dosežejo najvecjo vrednost, ce lahko
        na letalo natovorimo skupno tezo najvec "W".'''
    
    @lru_cache(maxsize=None)
    def najboljsi(i, w):
        if w < 0:
            return float("-inf"), 0
        if i == 0 or w == 0:
            return 0, 0
        neVzamemo, _ = najboljsi(i-1, w)
        vzamemo, _ = najboljsi(i-1, w-predmeti[i-1][1])
        # Tu se odlocimo, vzamemo predmet i samo takrat ko se nam dejansko splaca
        # Torej prioritiziramo predmete z manjšim indeksom. Lahko bi dali tudi >=
        if vzamemo + predmeti[i-1][0] > neVzamemo:
            return vzamemo + predmeti[i-1][0], 1
        return neVzamemo, 0
    
    # preberemo katere predmete smo vzeli
    i = len(predmeti)
    v = []
    
    while W > 0 and i > 0:
        # ali smo vzeli i-ti predmet
        _, vzamemo = najboljsi(i, W)
        if vzamemo:
            # dodamo ga v seznam in zmanjsamo volumen letala
            v.append(predmeti[i-1])
            W -= predmeti[i-1][1]
        i-=1
    return v
```
### **3. naloga**
Opis:

Trgovec je dobil dodatno pošiljko obstoječih predmetov. Tako ima sedaj na razpolago več kot en predmet posameznega tipa. Predmete tako predstavimo s seznamom elementov oblike (ci,vi,zi)
, kjer je: * ci
 cena * vi
 teža * zi
 zaloga i
-tega predmeta.

Implementiraj funkcijo optimalni_tovor_zaloga(predmeti, W), ki vrne največjo skupno ceno predmetov, ki jih lahko trgovec natovori na letalo z maksimalno nosilnostjo W. 

Koda:
```python
def optimalni_tovor_zaloga(predmeti, W):
    '''Vrne najvecjo skupno ceno predmetov, ki jih lahko
        trgovec natovori na letalo z maksimalno nosilnostjo "W".'''
    pomozni_sez = []
    for p in predmeti:
        for i in range(p[2]):
            pomozni_sez.append((p[0], p[1]))
    return optimalni_tovor(pomozni_sez, W)

```

### **4. naloga**
Opis:

Predpostavi, da ima sedaj trgovec na voljo neomejeno zalogo posameznih predmetov. implementiraj funkcijo neomejena_zaloga(predmeti, W), ki vrne najvišjo skupno ceno tovora na letalu z maksimalno nosilnostjo W.

Koda:
```python
def neomejena_zaloga(predmeti, W):
    @lru_cache(maxsize = None)
    def nahrbtnik(w):
        if w == 0: #prostora ni več
            return 0
        #vedno gremo čez vse predmete in enega vzamemo, pogledamo pa katerega se splača vzeti
        return max([nahrbtnik(w-v) + c for (c,v) in predmeti if v <= w] + [0])
    return nahrbtnik(W)
```


# VAJE 4
**Datum**: 8.3.2023

Na vajah smo na tabli reševali naloge v povezavi z množenji matrik. 
_________
### Komentarji in opombe
Naloge, ki smo jih reševali na vajah so se mi  zdele zelo zanimive. 
_______
### **1. naloga**
Spomnimo se problema matričnega množenja iz predavanj ter kako ga rešimo.

Opiši Bellmanovo enačbo oz. rekurzivno zvezo.

**Vhodni podatki:** matrike in njihove dimenzije 

$A_{1}A_{2}\dots A_{n-1}A_{n}$ in $d_{1} \dots d_{n-1}$

Pri čemer je: $dimA_{i}=d_{i} \times d_{i+1}$

**Izhodni podatki:** minimalno število množenj realnih števil za izračun produkta danih matrik $A_{1}A_{2}\dots A_{n-1}A_{n}$

**Bellmanova enačba:**
$$N(i,j) = min_{i \le k < j}(N(i,k) + N(k+1,j)+d_{i}\times d_{k+1} \times d_{j})$$

Robni pogoj: $i = j: N(i,i) = 0$

Izračunajte problem za produkt matrik velikosti: 3x5, 5x4, 4x2, 2x3, 3x5, 5x4, 4x6, 6x3 v tem vrstnem redu.

![Alt text](/Datoteke/vaje4_1.jpg)
![Alt text](/Datoteke/vaje4_2.jpg)

___________
### **2.naloga**
Recimo, da imamo izračunano tabelo $N(i,j) = (v, idx)$ iz Bellmanove enačbe, kjer je v optimalno število operacij, idx pa je seznam indeksov k, kjer je bil dosežen minimum pri združevanju podproblemov. Kako bi izračunal število vseh optimalnih produktov? Kakšna je časovna zahtevnost? Kaj pa če bi želel izpisati vse optimalne produkte?

$O(i,j)$= število optimalnih produktov matrik $A_{i} \dots A_{j}$

$O(i,i) = 1 $

$O(i, i+2) = 1$

$O(i,j) = \sum_{k \in N(i,j)[1]}O(i,k) \times O(k+1,j)  $ 

**Časovna zahtenost:** $O(n^2 \times n)$

 $n^2$ je število množenj, $n$ pa izračun trenutnega stanja
____________________
### **3. naloga**
V spodnji tabeli imamo že izveden izračun za vse vrednosti N(i,j) za matrike podanih velikosti, kjer matrike štejemo od 1 dalje. V tabeli je v (i,j)-ti celici prikazano min_operacij(index kjer je bil dosežen min) .

![Alt text](/Datoteke/vaje4_tabela1.png)

![Alt text](/Datoteke/vaje4_naloga3.jpg)
________________
### **4. naloga**

Podobno kot pri prejšnji nalogi imamo izračunano spodnjo tabelo (le da se to tabele številčijo od 0 naprej).

![Alt text](/Datoteke/vaje4_naloga4.png)

Odgovori na naslednja vprašanja:

- **Koliko operacij potrebujemo, da jih optimalno zmnožimo?**
  
  242

- **Kako jih mormao množiti?**

  $(A_{0}(A_{1}A_{2}))((((A_{3}A_{4})A_{5})A_{6})A_{7})$

- **Kako optimalno zmnožimo matrike od 3 do 7?****

  $((((A_{3}A_{4})A_{5})A_{6})A_{7})$

- **Koliko operacij potrebujemo, da optimalno zmnožimo prvih 5 matrik?**

  130

- **Kako naj zmnožimo zadnje štiri matrike, da bo število operacij najmanjše?**

    $N(5,8) = 168$

- **Ali si lahko pomagamo z izračunanimi podatki, če spremenimo število stolpcev zadnje matrike iz 3 na 4, da izračunamo novo optimalno množenje? Kaj moramo narediti?**


  Na novo bi morali izračunati samo zadnji stolpec od spodaj navzgor. 

### **5. naloga**

Pri tej nalogi bomo obravnavali primer, ko imamo na razpolago več kot en računalnik oziroma procesor. Kot vzorčni primer lahko vzamemo primer iz prejšnje naloge, bomo pa poizkušali povedat čim bolj splošno.

Predstavi nekaj strategij kako bi si pomagal z dodatnim računalnikom. Obravnavaj možnosti:

- en računalnik lahko obdela največ L (recimo 4) matrik.
- vseeno koliko matrik lahko obdela en računalnik.
- kaj če nas nekaj stane, da matriko prestavimo iz enega računalnika do drugega (recimo kopija matrike preko mreže v O(velikost matrike))?

Kaj se zgodi s številom operacij, ki jih moramo izvesti v zgornjih primerih? Ali se zmanjša/zveča? Kaj pa čas za izračun?

![Alt text](/Datoteke/vaje4_5.jpg)





