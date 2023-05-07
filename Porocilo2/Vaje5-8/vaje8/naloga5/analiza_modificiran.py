import timeit
import random
import BFS, djikstra, BFS_t, djikstra_t
import matplotlib.pyplot as plt

samples = [10**i for i in range(1, 6)]
bfs_times = []
bfs_t_times = []
djikstra_times = []
djikstra_t_times = []

for n in samples:
    # generirajmo naključen graf
    graph = [[] for _ in range(n)]
    for i in range(4*n):
        u = random.randint(0, n-1)
        v = random.randint(0, n-1)
        w = random.randint(1, 10)
        graph[u].append((v, w))

    rand = random.randint
    # čas BFS
    bfs_time = timeit.timeit(lambda: BFS.BFS(graph, 0), number=1)
    bfs_times.append(bfs_time)

    #čas BFS-t modificiran
    bfs_t_time = timeit.timeit(lambda: BFS_t.BFS_t(graph, 0, rand), number=1)
    bfs_t_times.append(bfs_t_time)

    # čas Djikstra
    djikstra_time = timeit.timeit(lambda: djikstra.djikstra(graph, 0), number=1)
    djikstra_times.append(djikstra_time)

    #čas Djikstra modificirana
    djikstra_t_time = timeit.timeit(lambda: djikstra_t.djikstra_t(graph, 0, rand), number=1)
    djikstra_t_times.append(djikstra_t_time)

# izrišimo graf
plt.plot(samples, bfs_times, label='BFS')
plt.plot(samples, djikstra_times, label="Dijkstra")
plt.plot(samples, bfs_t_times, label='BFS modificiran')
plt.plot(samples, djikstra_t_times, label="Dijkstra modificirana")
plt.xscale('log')
plt.yscale('log')
plt.xlabel('Število vozlišč')
plt.ylabel('Čas (sekunde)')
plt.title('Primerjava med Djikstro in BFS-jem in modificiranima algoritmoma')
plt.legend()
plt.show()
