# Vaje 7
**Datum:** 29/03/2023

**Avtor:** Filip Bojko

---

## **Naloga 1. Ponovitev od zadnjič**

>**FW:** $D_{ij}(k) = min \{D_{ij}(k-1), D_{ik}(k - 1) + D_{kj}(k-1)\}$\
$\Pi_{ij}(k) ...$ zadnje vozlišče na $i - j$ poti, kjer smemo vmes uporabiti samo vozlišča $1 ... k$

### **Začetni - robni pogoji:** 

>$\Pi{ii}(0) = i$\
$\Pi_{i, G(i)}(0) = i$\
$\Pi_{ij}(k) = \Pi_{ij}(k - 1)$\
$\Pi_{ij}(k) = \Pi_{k,j}(k - 1)$

### **Rekonstrukcija poti**

VHOD: vozlišča $i, j$, matrika $\Pi(n)$

IZHOD: najkrajša pot od $i$ do $j$



## **Python koda**
```python
    def FW() 
        p = j
        pot = []
        while p != i:
            pot.append(p)
            p = pi(i)(p)
        pot.append(i)
        return pot.reverse()
```
### **Časovna zahtevnost**
> $O(n) $

---
## **Naloga 2.**

### **Možne ideje**

1. Prištejemo povezave, ki kažejo v to vozlišče
2. Prištejemo povezave, ki kažejo ven iz vozlišča

Odločimo se glede na problem, smiselno obravnavamo začetno in končno vozlišče.

---

## **Naloga 3**

**Možne ideje:**
- Prištejemo povezave, ki kažejo v to vozlišče
- Prištejemo povezave, ki kažejo ven iz vozlišča

odločimo se glede na problem (smiselno obravnavamo začetno in končno vozlišče v poti).

V splošnem, je problem najdaljših poti zelo težek problem.

![](FWMax.png)
![](FWMax2.png)


Floyd Warshallov algoritem bi lahko uporabili pri iskanju najdaljših poti, saj ni negativnih ciklov.


---

## **Naloga 4**

|      |  EUR  |USD | YEN |
|:-:   | :-:   |:-: | :-: | 
| EUR  |1      | 1,2|     |
|USD   |       | 1  | 120 | 
| YEN  | 0,01  |    |  1  |


Sestavimo graf $G(V,e)$, kjer so:
>* Vozlišča: $(EUR,YEN,USD)$ - valute
>* Povezave: Pretvorba

Zanima nas najdražja pot v grafu od $ i $ do $j$.
To ceno bomo dobili kot produkt uteži na povezvah.

Utež na povezavah $i-j$ nastavimo na $-log(R_{i,j})$ --> iščemo najcenejšo pot od $i-j$ v tem grafu.

V ta namen želimo uporabiti Floyd Warshallov algoritem (to lahko naredimo, če graf nima negativnih ciklov).


Pokažimo, da jih naš graf res nima:


**DOKAZ S PROTISLOVJEM:**
Predpostavimo, da imamo negativen cikel od $i$ do $j$.
Cena tega cikla je: 

> $-(\sum_{j=1}^{k}log(R(i_{j-1},ij))) < 0 $  (pomnožimo enačbo z -1)\
>$-log(\Pi_{j=1}^{k} R(i_{j-1},ij)) < 0 / \cdot(-1)$\
>$log(\Pi_{j=1}^{k} R(i_{j-1},ij)) > 0$ (in dobimo)\
>$\Pi_{j=1}^{k} R(i_{j-1},ij)) > 1 $ ---> **TO JE ARBITRAŽA**


## **Naloga 5**

### **Vhodni podatki:**
>* Usmerjen graf $G(V,e)$
>* začetno vozlišče $s \in V$
>* $c_{i,j} \geq 0 $, cene so pozitivne

### **Izhodni podatki:**
>* cene najcenejših poti od $s$ do $i$ $\forall i \in V$ --> D
>* drevo najkrajših poti od $s$ do $i$ $\forall i \in V$ --> P

```python
def dijkstra(G,s):
    '''Vrne najkrajšo pot od s do vseh vozlišč v grafu G'''
    n = len(G)
    D = [float("inf")] * n
    P = [None] * n
    D[s] = 0 # D[i] pove razdaljo od s do i -> pri nas je i = s
    P[s] = s
    obiskani = [False] * n
    q = Vrsta(V(G))  # v vrsto dodamo še nedodana vozlišča  ... list[range(n)]

    while len(obiskani) != n:
        c = q.popmin()  # dobimo najmnajši element in ga odstrani iz seznama
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
pove, da pogledamo vsa vozlišča v q in vrnemmo tistega z najnižjim **D[]**

### **Časovna zatevnost:** 

$O(n)$ --obrazlaga--> do while zanke je $O(n)$, while zanka je $O(n)$ in for zanka je $O(n)$


