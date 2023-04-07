def seznam_povezav(ime_dat):
    '''Iz dane txt datoteke razbere povezave grafa, povezave doda v seznam `tocke` in jih uredi glede na začetna vozlišča.'''
    tocke = list()
    with open(ime_dat, 'r') as file:
        for vrstica in file:
            # če je vrstica začetna, ki nas ne zanima, jo spusti
            if '#' in vrstica:
                continue
            else:
                zacetek, konec = vrstica[:-1].split('\t')  # povezava
                tocke.append((int(zacetek), int(konec)))
    tocke = sorted(tocke, key=lambda x: x[0])  # uredimo tabelo povezav
    return tocke  # [(0, 1), (0, 2), (0, 29), (1, 0), (1, 23), (1, 32), (2, 0), (2, 26),...], integer
        
def ustvari_graf(povezave):
    graf = [list() for _ in range(povezave[-1][0]+1)]
    i = 0
    for tocka in povezave:
        if tocka[0] == i:
            graf[i].append((tocka[1], 1))
        else:
            i +=1
            graf[i].append((tocka[1], 1))
    return graf



def razberi(file):
    edges = list()
    n = 0
    with open(file, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if line[0] == '#':
                continue
            u, v = map(int, line.strip().split('\t'))
            n = max(n, u, v)
            edges.append((u,v))
    edges = sorted(edges, key=lambda x: x[0])
    return n, edges
    


#tab= seznam_povezav('roadNet-TX.txt')
#n, edges = razberi('roadNet-TX.txt')

