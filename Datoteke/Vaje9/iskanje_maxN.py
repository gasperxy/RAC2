import time
import random

from generiraj_graf_naloga2 import generiraj_graf
from generiraj_graf_naloga2 import zapisi_txt
from belman_ford_naloga3 import bellman_ford

def preberi_graf(ime):
    with open(ime, 'r') as dat:
        vrstice = dat.readlines()
        graf = [[] for _ in range(len(vrstice))]
        for vrstica in vrstice:
            u, v, w = map(int, vrstica.split())
            graf[u].append((v, w))
        return graf




N = 10000
while True:
    graf = generiraj_graf(N)
    zapisi_txt('graf', graf)
    graf = preberi_graf('graf.txt')

    start = time.time()
    bellman_ford(graf, 0)
    end = time.time()
    cas = end - start

    print(f"N = {N}, čas: {cas}")

    if cas > 1:
        print(f"Čas presegel 10 sekund za N = {N}")
        break

    N += 10000