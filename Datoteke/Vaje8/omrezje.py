from djikstra import djikstra


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
razdaljeDo, poti = djikstra(G, 100)

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



### 4. naloga
def najkrajsa_pot(s, t, drevo_najkrajsih):
    pot = [t]
    while pot[-1] != s:
        pot.append(drevo_najkrajsih[pot[-1]])
    return list(reversed(pot))


G = preberi_graf('roadNet-TX.txt')
razdalje, poti = djikstra(G, 100)
pot = najkrajsa_pot(100, 100000, poti)
print(pot)


# tab = omrezje(1393362)
# #graf2 = ustvari_graf(tab)
# razdalje, poti = djikstra(graf2, 100)
# print(razdalje[:6])  # prvih 5 
# 
# 
# rez = omrezje(1393362)
# print(rez[:10])
# 
# razdalje, poti = djikstra(rez, 100)
# print(razdalje,poti)
# 
# print(razdalje(100000))


# def naj():
#     with open('roadNet-TX.txt', 'r') as f:
#         vrstice = f.readlines()
#         veljavne = vrstice[4:]
#         maks = 0
#         for vrstica in veljavne:
#             trenutna = vrstica.strip().split('\t')
#         if int(trenutna[0]) > maks:
#             maks = int(trenutna[0])
#         if int(trenutna[1]) > maks:
#             maks = int(trenutna[1])
#     return maks
# 
# print(naj())
# 
# 
# 
# 
# def omrezje(n):
#     vse = [[] for _ in range(n+1)]
#     with open('roadNet-TX.txt', 'r') as f:
#         vrstice = f.readlines()
#         veljavne = vrstice[4:]
#         for vrstica in veljavne:
#             trenutna = vrstica.strip().split('\t')
#             od = int(trenutna[0])
#             do = int(trenutna[1])
#             if od > n:
#                 #print(od)
#                 continue
#             vse[od].append((1, do))
#     print('a')
#     return vse


# def read_graph(filename):
#     # read the file
#     with open(filename) as f:
#         lines = f.readlines()
# 
#     # extract the edges from the lines
#     edges = [tuple(map(int, line.strip().split())) for line in lines[2:]]
# 
#     # determine the number of nodes
#     num_nodes = max(max(edge) for edge in edges) + 1
# 
#     # construct the adjacency list
#     adj_list = [[] for _ in range(num_nodes)]
#     for u, v in edges:
#         adj_list[u].append((v, 1))  # assume all edges have weight 1
# 
#     return adj_list
