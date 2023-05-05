import matplotlib.pyplot as plt
import time
from djikstra import djikstra
from BFS import bfs_iskanje2
from fun_naloga3 import djikstra_koncna, bfs_iskanje_koncna


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


x4 = []
y4 = []

for i in [100, 1000, 10000, 100000, 1000000]:
    skupaj = 0
    for _ in range(6):
        zacetek = time.time()
        bfs_iskanje_koncna(rez, 100, i)
        konec = time.time()
        skupaj += konec-zacetek
    x4.append(i)
    y4.append(skupaj/6)


x3 = []
y3 = []

for i in [100, 1000, 100000, 1000000]:
    skupaj = 0
    for _ in range(6):
        zacetek = time.time()
        bfs_iskanje2(rez, 100)
        konec = time.time()
        skupaj += konec-zacetek
    x3.append(i)
    y3.append(skupaj/6)


x2 = []
y2 = []

for i in [100, 1000, 10000, 100000, 1000000]:
    skupaj = 0
    for _ in range(6):
        zacetek = time.time()
        djikstra_koncna(rez, 100, i)
        konec = time.time()
        skupaj += konec-zacetek
    x2.append(i)
    y2.append(skupaj/6)

x1 = []
y1 = []

for i in [100, 1000, 100000, 1000000]:
    skupaj = 0
    for _ in range(6):
        zacetek = time.time()
        djikstra(rez, 100)
        konec = time.time()
        skupaj += konec-zacetek
    x1.append(i)
    y1.append(skupaj/6)

plt.plot(x1, y1, label="djikstra samo začetek")
plt.plot(x2, y2, label="djikstra začetek in konec")
plt.plot(x3, y3, label="bfs samo začetek")
plt.plot(x4, y4, label="bfs začetek in konec")
plt.title("Časovna zahtevnost")
plt.legend()
# plt.savefig("cas_zahtevnost.pdf")
plt.show()
