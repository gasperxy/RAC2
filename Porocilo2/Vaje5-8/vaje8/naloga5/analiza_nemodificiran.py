import BFS, djikstra
import time

# Najprej bomo analizirali čas, ki ga Djikstra in BFS porabita na dani tekstovni datoteki.
# Naredimo graf iz roadNet.txt
seznam_sosedov = [[] for line in open("roadNet-TX.txt") if line[0] != "#" or line != "" ]
with open("roadNet-TX.txt", "r") as f:
    for line in f:
        if line[0] == "#" or line == "":
             continue
        vozlisca = line.split("\t")
        prvo_vozlisce = int(vozlisca[0].strip())
        drugo_vozlisce = int(vozlisca[1].strip())
        seznam_sosedov[prvo_vozlisce].append((drugo_vozlisce, 1))

# Izberimo začetno vozlišče
start_node = 0

# Izmerimo čas BFS-ja
start_time = time.time()
predhodniki = BFS.BFS(seznam_sosedov, start_node)
end_time = time.time()
bfs_time = end_time - start_time

# Izmerimo čas Djikstre
start_time = time.time()
predhodniki = djikstra.djikstra(seznam_sosedov, start_node)
end_time = time.time()
dijkstra_time = end_time - start_time

print("Čas porabljen BFS: %.6f sekund" % bfs_time)
print("Čas porabljen Dijkstra: %.6f sekund" % dijkstra_time)

import matplotlib.pyplot as plt


algorithms = ['BFS', 'Dijkstra']
times = [bfs_time, dijkstra_time]

# Izrišimo graf
fig, ax = plt.subplots()
ax.bar(algorithms, times)
ax.set_ylabel('Čas (sekunde)')
ax.set_title('Primerjava med BFS-jem in Djikstro')
plt.show()

import timeit
import random

samples = [10**i for i in range(1, 6)]
bfs_times = []
djikstra_times = []

for n in samples:
    # generirajmo naključen graf
    graph = [[] for _ in range(n)]
    for i in range(4*n):
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        w = random.randint(1, 10)
        graph[u].append((v, w))

    # čas BFS
    bfs_time = timeit.timeit(lambda: BFS.BFS(graph, 0), number=1)
    bfs_times.append(bfs_time)

    # čas Djikstra
    djikstra_time = timeit.timeit(lambda: djikstra.djikstra(graph, 0), number=1)
    djikstra_times.append(djikstra_time)

# izrišimo graf
plt.plot(samples, bfs_times, label='BFS')
plt.plot(samples, djikstra_times, label="Dijkstra")
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Število vozlišč')
plt.ylabel('Čas (sekunde)')
plt.title('Primerjava med Djikstro in BFS-jem')
plt.legend()
plt.show()