import matplotlib.pyplot as plt
import time
from djikstra import djikstra
from BFS import bfs_iskanje2
from fun_naloga3 import djikstra_koncna, bfs_iskanje_koncna


def omrezje2(n):
    vse = [[] for _ in range(n+1)]
    with open('roadNet-TX.txt', 'r') as f:
        vrstice = f.readlines()
        veljavne = vrstice[4:]
        for vrstica in veljavne:
            trenutna = vrstica.strip().split("\t")
            od = int(trenutna[0])
            do = int(trenutna[1])
            if do <= n and od <= n:
                vse[od].append((do, 1))
    return vse


vsi = []
for i in [1000, 2500, 5000, 9000, 40000, 100000, 250000]:
    vsi.append([omrezje2(i), i])

x4 = []
y4 = []

for rez, i in vsi:
    skupaj = 0
    for _ in range(6):
        zacetek = time.time()
        bfs_iskanje_koncna(rez, 0, 950)
        konec = time.time()
        skupaj += konec-zacetek
    x4.append(i)
    y4.append(skupaj/6)


x3 = []
y3 = []

for rez, i in vsi:
    skupaj = 0
    for _ in range(6):
        zacetek = time.time()
        bfs_iskanje2(rez, 0)
        konec = time.time()
        skupaj += konec-zacetek
    x3.append(i)
    y3.append(skupaj/6)


x2 = []
y2 = []

for rez, i in vsi:
    skupaj = 0
    for _ in range(6):
        zacetek = time.time()
        djikstra_koncna(rez, 0, 950)
        konec = time.time()
        skupaj += konec-zacetek
    x2.append(i)
    y2.append(skupaj/6)

x1 = []
y1 = []

for rez, i in vsi:
    skupaj = 0
    for _ in range(6):
        zacetek = time.time()
        djikstra(rez, 0)
        konec = time.time()
        skupaj += konec-zacetek
    x1.append(i)
    y1.append(skupaj/6)


with open("cas_DIJK_BFS", "a") as f:
    print(f"\n{'Število vozlišč':^20} | {'Število povezav':^20} | {'djikstra Z':^20} | {'djikstra Z/K':^20} | {'BFS Z':^20} | {'BFS Z/K':^20} |", file=f)
    print("-"*137, file=f)
    for i in range(len(x1)):
        print(
            f"{f'{x1[i]:,}':^20} | {f'{sum([len(el) for el in vsi[i][0]]):,}':^20} | {f'''{y1[i]:.15f} s''':<20} | {f'''{y2[i]:.15f} s''':<20} | {f'''{y3[i]:.15f} s''':<20} | {f'''{y4[i]:.15f} s''':<20} |", file=f)

plt.plot(x1, y1, label="djikstra samo začetek")
plt.plot(x2, y2, label="djikstra začetek in konec")
plt.plot(x3, y3, label="bfs samo začetek")
plt.plot(x4, y4, label="bfs začetek in konec")
plt.title("Časovna zahtevnost")
plt.legend()
# plt.savefig("cas_zahtevnost.pdf")
plt.show()
