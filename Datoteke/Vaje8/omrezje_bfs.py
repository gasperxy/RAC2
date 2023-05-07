from bfs import bfs

def preberi_graf(ime_datoteke):
    '''Iz datoteke prebere povezave grafa in jih zapiše v pravilno obliko (za G)'''
    with open(ime_datoteke, 'r') as f:
        vrstice = f.readlines()
    
    povezave = []
    for vrstica in vrstice[4:]:   #prve stiri vrstice so drugacne
        x, y = vrstica.strip().split()
        povezave.append((int(x), int(y)))
    # extract the edges from the lines
    #povezave = [tuple(map(int, line.strip().split())) for line in lines[4:]]    # if not line.startswith('#')]
    #print(povezave[:10])

    # poiščemo koliko je vseh vozlišč (največje + 1)
    st_vozlisc = max(max(povezava) for povezava in povezave) + 1    ## najprej pogleda katero vozlišče v posameznem tuplu je večje, potem pogleda največjega od njih

    # naredimo seznam sosedov (G)
    seznam_sosedov = [[] for _ in range(st_vozlisc)]
    for u, v in povezave:
        seznam_sosedov[u].append((v, 1))  # vse povezave imajo ceno 1

    return seznam_sosedov



G = preberi_graf("roadNet-TX.txt")
razdaljeDo, poti = bfs(G, 100)

#a
print(razdaljeDo[:10])  # prvih 10

#b
print(razdaljeDo[100000])

#c
naj_razdalja = max(razdaljeDo)
print(naj_razdalja)
najbolj_oddaljeno_vozlisce = razdaljeDo.index(naj_razdalja)
print(najbolj_oddaljeno_vozlisce)

#d
st_dosegljivih = sum(1 for razdalja in razdaljeDo if razdalja != -1)
print(st_dosegljivih)

naj_razdalja = min(razdaljeDo)
print(naj_razdalja)
        