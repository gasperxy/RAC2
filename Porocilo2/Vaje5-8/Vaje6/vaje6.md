# Vaje 6
**Datum:** 22/03/2023

**Avtor:** Filip Bojko

---


## **BFS**

**BFS** - "Breadth first-search"\
**DFS** - "Depth first-search"

Mi se bomo osredotočili na **BFS**:

- pregled grafa
- vpeto drevo/gozd v grafu povezane komponente
- preverjanje dvodelnosti grafa
- iskanje najkrajših poti (neuteženem grafu)

## **Python koda**
```python
    def BFS(G, u) 
        # G: graf kot seznam sosedov 
        # u: začetno vozlišče
        n = len(G)
        obiskani = [False] * n
        #DFS: spremenimo v sklad()
        q = Vrsta([u]) # začnemo v u (v py: from collections import deque)
        while q:
            trenutni = q.popleft()
        if obiskani[trenutni] = True
        for sosed in G[trenutni]:
            if not obiskani[sosed]:
                #Lahko tudi q.append(sosed)
                q.push(sosed)
```
---
## **Naloga 1.**
Za iskanje poti

```python
    def BFS(G,u):
    '''Vrne najkrajše poti od u do vseh ostalih poti'''
    n = len(G)
    d = [0] * n # čz: O(n + m) n ... število vozlišč m ... število povezav
    obiskani = [False] * n # nobenega vozlišča še nismo obiskali

    #    deque( ) --> knjiznica Deque
    q = vrsta([(u,0)])  # v vrsto damo vozlišče u in razdaljo od u do u (0)

    while q:  # dokler vrsta ni prazna
        trenutni, razdalja = q.popleft()
        
        if obiskani[trenutni] : continue # soseda smo že obiskali
        obiskani[trenutni] = True
        d[trenutni] = razdalja

        for sosed in G[trenutni]:
            if not obiskani[sosed]:
                q.push(sosed, razdalja + 1) # doda v vrsto
```
### **Časovna zahtevnost**
```O(n + m)```

n ... število vozlišč 

m ... število povezav

---
## **Naloga 2.**

**Floyd-Warshallow algoritem**

>**Vhod:** Graf G, utežen(dovoljene so negativne uteži)\
>**Izhod:** D dimenzije **n x n** (**n** je število vozlišč)

$D_j$ je cena najkrajše poti med i-tim in j-tim vozliščem

### **Ideja**

$D_{ij}(k) = min \{D_{ij} D_{ik} + D_{kj} \}$

isto kot $D_{ij}$, samo da uporabljamo vozlišča med 1 in K

>**Robni pogoji**  
> $D_{ii} = 0$\
> $D_{1i} = \omega _{1i}$ (utež povezave)

>**Časovna zahtevnost** 
> O($n^3$)

## **Naloga 3.**

|   | 1      | 2      | 3      | 4      | 5      |
|---|--------|--------|--------|--------|--------|
| 1 | 0      | 2      | $\infty$, 3 | 8, 5      | $\infty$, 7 |
| 2 | $\infty$, 8, 6 | 0      | 1      | $\infty$, 3 | $\infty$, 5 |
| 3 | $\infty$, 7, 5 | $\infty$, 0 | 0      | 2      | $\infty$, 4 |
| 4 | $\infty$, 5, 3 | -2     | $\infty$, -1 | 0      | 2      |
| 5 | 1      | 7, 3, -3      | -3     | $\infty$, 9, -1 | 0      |