from fun_naloga3 import djikstra_koncna, bfs_iskanje_koncna
from fun_naloga4 import pot


def naj():
    naj = 0
    with open('roadNet-TX.txt', 'r') as f:
        vrstice = f.readlines()
        veljavne = vrstice[4:]
        for vrstica in veljavne:
            trenutna = vrstica.strip().split("\t")
            od = int(trenutna[0])
            do = int(trenutna[1])
            if od > naj:
                naj = od
    return naj


def omrezje(n):
    vse = [[] for _ in range(n+1)]
    with open('roadNet-TX.txt', 'r') as f:
        vrstice = f.readlines()
        veljavne = vrstice[4:]
        for vrstica in veljavne:
            trenutna = vrstica.strip().split("\t")
            od = int(trenutna[0])
            do = int(trenutna[1])
            vse[od].append((do, 1))
    return vse


rez = omrezje(naj())

# naloga 3

razdalje3, poti3 = djikstra_koncna(rez, 100, 100000)
print(razdalje3[100000])

razdalje4, poti4 = bfs_iskanje_koncna(rez, 100, 100000)
print(razdalje4[100000])


# ===============================================
# naloga 4

print(pot(100, 100000, djikstra_koncna(omrezje(naj()), 100, 100000)[1]))
