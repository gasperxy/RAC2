from BF_algoritem import BF, BF_ustavitev
import time
from BFS import bfs_iskanje2
from djikstra import djikstra


def omrezje(n):
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


with open("cas_BF_BFS", "a") as f:
    print(f"\n{'Število vozlišč':^20} | {'Število povezav':^20} | {'BFS':^20} | {'BF':^20}", file=f)
    print("-"*90, file=f)
for i in range(10000, 300001, 10000):
    rez = omrezje(i)
    z = time.time()
    raz1, pot1 = bfs_iskanje2(rez, 0)
    k = time.time()
    z2 = time.time()
    raz2, pot2 = BF_ustavitev(rez, 0)
    k2 = time.time()
    # z3 = time.time()
    # raz3, pot3 = djikstra(rez, 0)
    # k3 = time.time()
    # print(
    #     f"Če izberemo prvih {i}. vozlišč\nimamo {sum([len(el) for el in rez])} povezav\nBF algoritem potrebuje {k-z} in {k2-z2}s\n{raz1==raz2}\n\n")
    # print(
    #     f"Če izberemo prvih {i}. vozlišč imamo {sum([len(el) for el in rez])} povezav\nDjikstra {k3-z2}\nBF_ustavitev {k2-z2}\nBFS {k-z}s\n\n")
    # print(
    #     f"Če izberemo prvih {i}. vozlišč\nimamo {sum([len(el) for el in rez])} povezav\nBF_ustavitev {k2-z2}\nBFS {k-z}s\n{raz1==raz2}\n")
    with open("cas_BF_BFS", "a") as f:
        print(
            f"{f'{i:,}':^20} | {f'{sum([len(el) for el in rez]):,}':^20} | {f'''{k2-z2:.15f} s''':<20} | {f'''{k-z:.15f} s''':<20}", file=f)
