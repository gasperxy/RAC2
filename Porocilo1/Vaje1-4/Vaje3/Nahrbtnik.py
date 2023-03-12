#NALOGA 1
def optimalni_tovor(predmeti, W):
    n = len(predmeti)
    V = [[0 for _ in range(W+1)] for _ in range(n+1)]
    
    for i in range(1, n+1):
        c_i, v_i = predmeti[i-1]
        for j in range(1, W+1):
            if v_i > j:
                V[i][j] = V[i-1][j]
            else:
                V[i][j] = max(V[i-1][j], c_i + V[i-1][j-v_i])
    
    return V[n][W]

#NALOGA 2
def krneki(predmeti, W):
    n = len(predmeti)
    matrika = [[0 for _ in range(W+1)] for _ in range(n+1)]
    sledilna_matrika = [[0 for _ in range(W+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, W+1):
            cena, teza = predmeti[i-1]
            if j >= teza and matrika[i-1][j-teza] + cena > matrika[i-1][j]:
                matrika[i][j] = matrika[i-1][j-teza] + cena
                sledilna_matrika[i][j] = 1
            else:
                matrika[i][j] = matrika[i-1][j]
    return matrika, sledilna_matrika

def optimalni_predmeti(predmeti, W):
    matrika, sledilna_matrika = krneki(predmeti, W)
    i, j = len(predmeti), W
    izbrani_predmeti = []
    while i > 0 and j > 0:
        if sledilna_matrika[i][j] == 1:
            cena, teza = predmeti[i-1]
            izbrani_predmeti.append((cena, teza))
            j -= teza
        i -= 1
    izbrani_predmeti.reverse()
    return izbrani_predmeti

#NALOGA 3
def optimalni_tovor_zaloga(predmeti, W):
    n = len(predmeti)
    zaloge = []
    for i in range(n):
        for j in range(1, predmeti[i][2] + 1):
            zaloge.append((predmeti[i][0], predmeti[i][1]))
    return optimalni_tovor(zaloge, W)

#NALOGA 4
def neomejena_zaloga(predmeti, W):
    # seznam, ki bo vseboval maksimalno vrednost za posamezno nosilnost od 0 do W
    vrednosti = [0] * (W + 1)

    # za vsako nosilnost od 0 do W izračunamo maksimalno vrednost
    for w in range(1, W + 1):
        for c, v in predmeti:
            # če lahko predmet spravimo v letalo
            if w >= v:
                # izračunamo novo vrednost, ki bi jo dobili, če bi predmet dodali v tovor
                nova_vrednost = vrednosti[w - v] + c

                # če je nova vrednost večja od trenutne, jo uporabimo
                if nova_vrednost > vrednosti[w]:
                    vrednosti[w] = nova_vrednost

    # na koncu vrnemo maksimalno vrednost, ki jo lahko natovorimo na letalo
    return vrednosti[W]