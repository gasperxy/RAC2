def topo_sort(G):
    n = len(G)
    # in_deg[i]...št. povezav, ki kaže v i
    in_deg = [0]*n
    for i in range(n):
        for j in range(G[i]):
            in_deg[j] += 1
    rezultat = []
    izvori = [i for i in range(n) if deg[i]==0]
    while izvori:
        izvor = izvori.pop()
        rezultat.append(izvor)
        for sosed in G[izvor]:
            in_deg[sosed] -= 1
            if in_deg[sosed] == 0:
                izvor.append(sosed)
    return rezultat




