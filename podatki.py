def podatki():
    sez = []
    n = 0
    with open("roadNet-TX.txt", 'r') as dat:
        vrstice = dat.readlines()
        veljavne = vrstice[4:]
        for vrstica in veljavne:
            vrst = vrstica.strip().split('\t')
            u, v = [int(el) for el in vrst]
            n = max(n,u,v)
            sez.append((u, v))
    return n, sez

def UstvariGraf(n, seznam):
    G = [[] for _ in range(n+1)]
    
    for u,v in seznam:
        G[u].append((v, 1))
    return G