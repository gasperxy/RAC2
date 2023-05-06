import random

def generiraj_graf(n):
    graf=list()
    for vozlisce in range(n+1):
        tab = list()
        for sosed in range(random.randint(1,n+1)):
            tab.append((random.randint(0,n), random.randint(1,10)))
        graf.append(tab)
    return graf


def zapisi_txt(ime, graf):
    with open(ime + '.txt', 'w') as dat:
        for ind, sosedje in enumerate(graf):
            for sosed in sosedje:
                vrstica = '{} {} {}\n'
                dat.write(vrstica.format(ind, sosed[0], sosed[1]))


g1 = generiraj_graf(49)
zapisi_txt('graf_g1', g1)