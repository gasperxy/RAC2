import random

def generiraj_graf(n):
    graf = [[] for _ in range(n+1)]
    for u in range(n+1):
        for v in range(n+1):
            if u != v and random.random() < 0.2:   # z 20% moznostjo bomo dodali vozlisce kot soseda
                w = random.randint(1, 10)
                graf[u].append((v, w))
    return graf

def zapisi_txt(ime, graf):
    with open(ime + '.txt', 'w') as dat:
        for u, sosedje in enumerate(graf):
            for v, w in sosedje:
                vrstica = '{} {} {}\n'.format(u, v, w)
                dat.write(vrstica)

G = generiraj_graf(49)
zapisi_txt('graf_G', G)

