def BFS(G, s):
    '''vrne najkrajše poti od u do vseh vozlisc'''
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



def seznam_sosednosti(seznam):
    '''Funkcija, ki spremeni seznam parov sosednjih vozlišč v seznam sosednosti z utežjo 1.'''
    matrika = [list() for _ in range(seznam[-1][0] + 1)] # toliko je vseh vozlišč
    for i,j in seznam:
        matrika[i].append((j,1))
    return matrika


primer1 = datoteka("roadNet-TX.txt")
graf = seznam_sosednosti(primer1)
najkrajse_razdalje_od_sto, poti = BFS(graf, 100)
print(najkrajse_razdalje_od_sto)
# razdalja dG(100,100000)
dG = najkrajse_razdalje_od_sto[100000]
print(dG)
# Katero vozlišče je najbolj oddaljeno od vozlišča 100
najvecja_razdalja = max(najkrajse_razdalje_od_sto)
ind = najkrajse_razdalje_od_sto.index(najvecja_razdalja)
print(ind)
# Koliko vozlišč je dosegljivih iz vozlišča 100?
def koliko_vozlisc(seznam):
    stevec = 0
    for i in seznam:
        if i >= 1:
            stevec += 1
    return stevec

print(koliko_vozlisc(najkrajse_razdalje_od_sto))