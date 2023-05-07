# def bellman_ford(graf, zacetna_tocka):
#     razdalje = {tocka: float('inf') for tocka in graf}
#     razdalje[zacetna_tocka] = 0
# 
#     for _ in range(len(graf) - 1):
#         for tocka in graf:
#             for sosed in graf[tocka]:
#                 nova_razdalja = razdalje[tocka] + sosed[1]
#                 if nova_razdalja < razdalje[sosed[0]]:
#                     razdalje[sosed[0]] = nova_razdalja
# 
#     for tocka in graf:
#         for sosed in graf[tocka]:
#             if razdalje[tocka] + sosed[1] < razdalje[sosed[0]]:
#                 return None
# 
#     return razdalje
# 
# def Bellman_Ford(graf, zacetek, n):
#     razdalje = [float('inf')] * n
#     razdalje[zacetek] = 0
# 
#     for korak in range(n-1):
#         for u, v, w in graf:
#             if razdalje[u] + w < razdalje[v]:
#                 razdalje[v] = razdalje[u] + w
# 
#     for u, v, w in graf:
#         if razdalje[u] != float('inf') and razdalje[u] + w < razdalje[v]:
#             return None
# 
#     return razdalje
# 
# def Bellman_Ford(graf, zacetek, n):
#     razdalje = [float('Inf')]*n
#     razdalje[zacetek] = 0
#     
#     for korak in range(n-1):
#             if razdalje[u] + w < razdalje[v]:
#                 razdalje[v] = razdalje[u] + w
#     for u, v, w in graf:
#         if razdalje[u] != float('Inf') and razdalje[u] + w < razdalje[v]:
#             return None
#     return razdalje

def bellman_ford(graf, zacetek):
    n = len(graf) - 1
    razdalje = [float('Inf')] * (n+1)
    razdalje[zacetek] = 0
    
    for korak in range(n-1):
        for u in range(n+1):
            for v, w in graf[u]:
                if razdalje[u] + w < razdalje[v]:
                    razdalje[v] = razdalje[u] + w
    
    for u in range(n+1):
        for v, w in graf[u]:
            if razdalje[u] != float('Inf') and razdalje[u] + w < razdalje[v]:
                return None
    
    return razdalje[1:]

with open('graf_G.txt', 'r') as dat:
    graf = [[] for _ in range(50)]
    for vrstica in dat:
        u, v, w = map(int, vrstica.strip().split())
        graf[u].append((v, w))

    zacetek = 0
    razdalje = bellman_ford(graf, zacetek)
    print(razdalje)