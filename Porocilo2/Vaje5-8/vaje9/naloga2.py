def preberi_graf(ime_datoteke):
    # naredimo prazen graf
    graf = {}

    # preberimo datoteko vrstico po vrstici
    with open(ime_datoteke) as f:
        for line in f:
            # razbijmo vrstico
            vozlisce, sosedje, teza = line.strip().split()
            vozlisce = int(vozlisce)
            sosedje = [int(s) for s in sosedje.split(',')]
            teza = int(teza)

            # dodajmo povezavo v graf
            graf[vozlisce] = dict(zip(sosedje, [teza]*len(sosedje)))
    
    return graf

def bellman_ford(graf, zacetek):
    # inicialniziramo razdalje in predhodnike
    razdalje = {vozlisce: float('inf') for vozlisce in graf}
    predhodniki = {vozlisce: None for vozlisce in graf}
    razdalje[zacetek] = 0

    for i in range(len(graf) - 1):
        for u in graf:
            for v, teza in graf[u].items():
                if razdalje[u] + teza < razdalje[v]:
                    razdalje[v] = razdalje[u] + teza
                    predhodniki[v] = u

    # Poglejmo ali graf vsebuje negativne cikle
    for u in graf:
        for v, teza in graf[u].items():
            if razdalje[u] + teza < razdalje[v]:
                raise ValueError('Graf vsebuje negativni cikel')

    return razdalje, predhodniki

graf = preberi_graf('graf.txt')
zacetek = 6
razdalje, predhodniki = bellman_ford(graf, zacetek)
print('Razdalje:', razdalje)
print('Predhodniki:', predhodniki)