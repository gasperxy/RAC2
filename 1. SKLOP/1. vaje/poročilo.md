# Dinamično programiranje in časovna zatevnost

**Ime:** Hana Lukež

**Datum:** 25.2.2023

---
## <span style="color: red">1. Naloga</span>

### __Navodilo__
Ponovitev časovne zahtevnosti in O notacije.

Za podatkovne strukture v pythonu seznam, slovar in verižni seznam zapiši njihove časovne zahtevnosti za:

dodajanje na začetku/sredini/koncu
poizvedbe
iskanje
brisanje začetku/sredini/koncu

### __Reševanje__

| pod.struktura     |  dodaj(n)  |  dodaj(i)  |  dodaj(0)  |  dostop(i)  |  "x in ?"  |  briši(0)  |  briši(i) | briši(n)	|
|---|---|---|---|---|---|---|---|---|
| seznam	    	|    O(1)    |    O(n)    |     O(n)   |    O(1)     |    O(n)    |    O(n)    |    O(1)    |    O(1)	|
| slovar/množica    |    O(1)    |    O(1)    |    O(1)    |    O(1)     |    O(1)    |    O(1)    |    O(1)    |    O(1)   |
| verižni seznam    |    O(1)    |    O(1)    |    O(1)    |    O(n)     |    O(n)    |    O(1)    |    O(1)    |    O(1)   |
| veriga vozlov     |    O(n)    |    O(n)    |    O(1)    |    O(n)     |    O(n)    |    O(n)    |    O(n)    |    O(n)   |
 




### __Komentarji__
- slovar in množica imata oba v implementaciji hash funkcijo --> zato imajo vse operacije konstantno časovno zahtevnost



## <span style="color: red">2. Naloga</span>

### __Navodilo__
Reševanje nalog iz sklopa https://www.projekt-tomo.si/problem_set/2558/.

Na tablo bomo najprej skupaj rešili nekaj nalog iz dinamičnega programiranja. Nato boste probali sami rešit naloge iz projekta Tomo (zgornji link).

V poročilo vključite vsaj eno nalogo iz tega sklopa, ki ste jo rešili z rekurzijo in brez nje. 


### __Reševanje__
Rešila sem nalogo jajce iz Tomota. 

_Navodilo : Visoka stavba ima več nadstropij. Sprehajamo se od nadstropja do nadstropja ter pri tem iz nekega nadstropja lahko spustimo jajce, ki pada do tal. Jajce se bodisi razbije bodisi ostane celo. Celo jajce lahko poberemo in ga ponovno uporabimo. Če se jajce razbije v nekem nadstropju se razbije tudi v vseh višjih nadstropjih, velja pa tudi obratno. Želimo ugotoviti, katero je najnižje nadstropje v katerem se jajce še razbije. Na voljo imamo k
 jajc stavba pa ima n
 nadstropij. Kolikšno je najmanjše število metov jajca, da bomo zagotovo ugotovili katero je ''kritično'' nadstropje._


#### __Brez rekurzije__

```python
def jajce_iter(n, k):
    # tabela za hranjenje najmanjšega števila metov jajca v vsakem nadstropju za dano število jajc
    tab = [[0] * (k + 1) for _ in range(n + 1)]

    # osnovni primeri: če imamo samo eno jajce, moramo jajce metati vse do najvišjega nadstropja
    # če imamo samo eno nadstropje, potem ne rabimo metati jajca
    for i in range(1, n + 1):
        tab[i][1] = 1
    for j in range(1, k + 1):
        tab[1][j] = j

    # izračunajmo preostale vrednosti v tabeli z uporabo prejšnjih vrednosti
    for i in range(2, n + 1):
        for j in range(2, k + 1):
            # predpostavimo, da se bo jajce razbilo pri metu iz x-tega nadstropja
            # potem imamo dve možnosti:
            #   1. jajce se razbije, torej moramo iskati kritično nadstropje v podintervalu [1, x-1] z uporabo manj jajc (n-1)
            #   2. jajce ostane celo, torej moramo iskati kritično nadstropje v podintervalu [x+1, n] z enakim številom jajc (n)
            # izberemo tisto, ki bo zahtevala največje število metov jajca (tj. najslabši možni scenarij)
            tab[i][j] = float('inf')
            for x in range(1, j + 1):
                tab[i][j] = min(tab[i][j], 1 + max(tab[i - 1][x - 1], tab[i][j - x]))

    return tab[n][k]

```



#### __Z rekurzijo__




```python
from functools import lru_cache

@lru_cache(maxsize=None)
def jajce_rec(n,k):
    if n == 1:
        return k
    if k == 1:
        return 1
    if k == 0:
        return 0
    else:
        return min(max(jajce_rec(n-1,i-1),jajce_rec(n,k-i)) for i in range(1,k+1)) + 1
```


#### __Ideja reševanja__

Naj bo:
n...število jajc
k...število nadstropij
- prva ideja je bila bisekcija. Ne bo vredu v primeru kadar imamo na razpolago samo eno jajce
- če imamo na razpolago eno jajce, potem moramo od spodaj navzor za vsako nadstropje preveriti ali se jajce razbije ali ne
- če imamo eno nadtropje, potem iamamo dovolj eno jajce
- imamo dve možnosti: jajce se NE razbije na i-jtem nadstropju ( v tem primeru imamo še vedno enako število jajc na voljo, vendar število nadstropij za preveriti se nam zmanjša za ena) in jajce SE razbije na i-tem nadstropju (v tem primeru smo izgubili eno jajce)

























