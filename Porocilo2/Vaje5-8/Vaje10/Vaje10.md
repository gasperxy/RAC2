# Vaje10
 
## **Kopica**

### **(Min) Binarna kopica**
Lasnosti:
- levo poravnano
- lastnost kopice: "$starš \leq sin$"

T je seznam dolžine n (kopica)

$T[i]$ - vozlišče

Sinovi od $i$ so $2i$ in $2i + 1$.

Če je prvi $i = 1$:

    starš $i // 2$

Če prvi $i = 0$:

    sinova $2i + 1$ in $2i + 2$
    starš $(i - 1) // 2

Python koda: 

```python
def push(T, x):
    #minimalna kopica
    T.append(x)
    i = len(T) - 1
    oce = i // 2
    while T[oce] > T[i]:
        T[oce], T[i] = T[i], T[oce]
        i = oce
        oce = i // 2
```

```python
def pop(T):
    #Odstranimo koren
    koren = T[1]
    T[1] = T[-1]
    T.pop()
    levi_sin = 2 * i
    desni_sin = 2 * i + 1
    while T[i] > T[levi_sin] or T[i] > T[desni_sin]:
        if T[levi_sin] > T[desni_sin]
            T[desni_sin], T[i] = T[i], T[desni_sin]
            i = desni_sin
            levi_sin = 2 * i
            desni_sin = 2 * i + 1
        else:
            T[levi_sin], T[i] = T[i], T[levi_sin]
            i = levi_sin
            levi_sin = 2 * i
            desni_sin = 2 * i + 1
    return koren

```

Časovna zahtevnost ``pop()`` in ``push()`` je $O(log(n))$

## **3.Naloga**

### **Heapify**
iz seznama v kopico

1.  Seznam tretiramo kot kopico

        LPDD: imamo
        Lastnost kopice: nimamo

### **Časovna zahtvnost** (shift up)

$\sum_{i=0}^{L(\log{n})} 2^{i} * i = \sum_{i=0}^{n - 1} i * \log{i} = O(n \log{n})$

### **Časovna zahtvnost** (shift down)

$\frac{n}{2} * 0 + \frac{n}{4} * 1 + \frac{n}{8} * 2 + ... \leq \sum_{i=1}^{\log{n}} \frac{n}{2^i} *(i - 1) = \sum_{i=0}^{L(\log{n})} \frac{n}{2^(i + 1)} * i \leq \frac{n}{2} \sum_{i=1}^{\inf} i * 2^-1 \leq \frac{n}{2} = n$