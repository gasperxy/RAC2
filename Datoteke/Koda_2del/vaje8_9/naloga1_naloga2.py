from python3 import omrezje, naj
from BFS import bfs_iskanje2
from djikstra import djikstra


seznam = omrezje(naj())

razdalje, poti = djikstra(seznam, 100)
# print(f"Najkrajše razdalje od vozlišča 100 do vseh ostalih: \n{poti}\n")

print(f"Razdalja od 100 do 100000: \n{razdalje[100000]}\n")

naj = razdalje.index(max(razdalje))

print(f"Najbolj oddaljeno vozlišče od vozlišča 100: {naj}\n")

koliko = sum([1 for el in razdalje if el > 0])

print(f"{koliko} vozlišč je dosegljivih iz vozlišča 100\n")

# =========================================================
print()
razdalje2, poti2 = bfs_iskanje2(seznam, 100)

# print(f"Najkrajše razdalje od vozlišča 100 do vseh ostalih: \n{poti2}\n")

print(f"Razdalja od 100 do 100000: \n{razdalje2[100000]}\n")

naj2 = razdalje2.index(max(razdalje2))

print(f"Najbolj oddaljeno vozlišče od vozlišča 100: {naj2}\n")

koliko2 = sum([1 for el in razdalje2 if el > 0])

print(f"{koliko2} vozlišč je dosegljivih iz vozlišča 100")
