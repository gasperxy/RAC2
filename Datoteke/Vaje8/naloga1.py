import djikstra

def seznam_sosednosti():
    """
    Iz grafa zapisanega v .txt datotek ustvari seznam sosednosti.
    """
    with open("roadNet-TX.txt", "r") as f:
        vrstice = f.readlines()[4:]
    n = max({int(vrstica.split("\t")[0]) for vrstica in vrstice})
    G = [[] for _ in range(n + 1)]
    for vrstica in vrstice:
        u, v = vrstica.strip().split("\t")
        G[int(u)].append((int(v), 1))
    return G

if __name__ == "__main__":
    razdalje, poti = djikstra.djikstra(seznam_sosednosti(), 100)
    print(razdalje[100000])
    # Najbolj oddaljeno vozlišče
    max_d = max(razdalje)
    max_vozlisca = [i for i in range(len(razdalje)) if razdalje[i] == max_d]
    print(max_vozlisca)
    # Koliko vozlišč je dosegljivih iz 100
    st_dosegljivi = len([d for d in razdalje if d > -1])
    print(st_dosegljivi)