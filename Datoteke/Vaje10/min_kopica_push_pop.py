def push(T, x):
    '''
        Funkcija v seznam `T`, ki predstavlja minimalno kopico, doda vozlišče `x`.
    '''
    T.append(x)  # dodamo na konec seznama
    i = len(T) - 1  # dobimo indeks od x-a
    stars = i//2  # koren na i=1
    while T[stars] >= T[i]:
        # ker imamo minimalno kopico in je vrednost očeta
        # večja ali enaka od sina, ju zamenjamo
        T[stars], T[i] = T[i], T[stars]
        i = stars
        stars = i//2
        
def pop(T):
    '''
        Funkcija vrne in odstrani koren dane kopice, predstavljeno kot seznam `T`, in jo popravi tako,
        da ohrani pogoje minimalne kopice.
    '''
    koren = T[1]  # prvi element seznama odmislimo
    T[1] = T[-1]  # koren zamenjamo z najbolj levim listom t.j. zadnji element v seznamu)
    
    T.pop()  # odstranimo zadnji element (to ni ista naša funkcija)
    
    i = 1  # začnemo pri korenu
    levi_sin = 2*i
    desni_sin = 2*i + 1
    while T[i] > T[levi_sin] or T[i] > T[desni_sin]:
        # ponavljamo, dokler ne bo veljalo pravilo za minimalno kopico (starš <= sin)
        # starša zamenjamo z manjšim od sinov
        
        if T[levi_sin] > T[desni_sin]:
            # menjava z desnim sinom
            T[desni_sin], T[i] = T[i], T[desni_sin]
            i = desni_sin
        else:
            # menjava z levim sinom
            T[levi_sin], T[i] = T[i], T[levi_sin]
            i = levi_sin
        
        levi_sin = 2*i
        desni_sin = 2*i + 1
    return koren

    
    

