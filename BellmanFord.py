def BellmanFord(graf, zac, n):
    '''Implementacija Bellman fordovega algoritma'''
    razdalje = [float("Inf")] * n #n predstavlja stevilo vozlov v grafu
    razdalje[zac] = 0

    for _ in range(n - 1):
        spremenba = False
        for u, v, w in graf:
            if razdalje[u] != float("Inf") and razdalje[u] + w < razdalje[v]: #Ali obstaja bliznjica?
                spremeba = True
                razdalje[v] = razdalje[u] + w
        if not spremenba:
            break

    for u, v, w in graf: #Preverimo negativne cikle.
        if razdalje[u] != float("Inf") and razdalje[u] + w < razdalje[v]:
            print("Graf vsebuje negativen cikel.")
            return None
        
    return razdalje

def podatki():
    sez = []
    with open("podatki_graf.txt", 'r') as dat:
        for vrstica in dat:
            zac, konc, utez = vrstica.strip().split(' ')
            sez.append((int(zac), int(konc), int(utez)))
    return sez
if __name__ == "__main__" :
    razdalje = BellmanFord(podatki(), 0, len(podatki()))
    print(razdalje)