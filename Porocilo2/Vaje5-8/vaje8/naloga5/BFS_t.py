from collections import deque

def BFS_t(G, s, t):
    """
    BFS vrne najkrajše poti od s do vseh ostalih vozlišč. Tu je s štartno 
    vozlišče, G pa je graf, ki je podan kot seznam sosednosti. Seznam d 
    predstavlja najkrajšo pot od vozlišča s do vseh ostalih. Poleg tega 
    sprejme tudi končno vozlišče t in vrne najcenejšo razdaljo
    od s do t. Prav tako vrne drevo najkraših poti kot seznam, kjer
    je i-ti element oče vozlišča i-1.
    """
    n = len(G)

    # Nastavimo začetne vrednosti za sezname d, obiskani, in poti.
    d = [0] * n  
    obiskani = [False] * n
    poti = [-1] * n

    # Na vrsto dodamo trojico (v, d, p), kjer je: v vozlišče, d je razdalja, p 
    # pa prejšnje vozlišče na najkrajši poti od u do v.
    q = deque([(s, 0, s)])

    while q:
        u, razdalja, p = q.popleft()

        if obiskani[u]: 
            continue # smo ga že obiskali
        
        # obiščemo vozlišče ter nastavimo njegovo razdaljo
        # ter predhodnika na najkrajši poti od s do u
        obiskani[u] = True
        d[u] = razdalja
        poti[u] = p

        # če smo prišli do vozlišča s, skonstruiramo drevo poti
        # in vrnemo najcenejšo razdaljo od s do t
        if u == t:
            pot_do_t = [t]
            pred = poti[t]
            while pred != s:
                pot_do_t.append(pred)
                pred = poti[pred]
            pot_do_t.append(s)
            return d[t], pot_do_t

        # gremo čez vse sosede in dodamo potrebne elemente na vrsto.
        for sosed in G[u]:
            if not obiskani[sosed[0]]:
                q.append((sosed[0], razdalja + 1, u)) #doda nov element v q
    return d, poti

#Podatkovna struktura grafa
#seznam_sosedov = [[] for line in open('C:/Users/filip/OneDrive/Desktop/Šola/Rač2/RAC2/Porocilo2/Vaje5-8/vaje8/naloga1/roadNet-TX.txt', "r") if line[0] != "#" or line != "" ]
#with open('C:/Users/filip/OneDrive/Desktop/Šola/Rač2/RAC2/Porocilo2/Vaje5-8/vaje8/naloga1/roadNet-TX.txt', "r") as f:
#    for line in f:
#        if line[0] == "#" or line == "":
#             continue
#        vozlisca = line.split("\t")
#        prvo_vozlisce = int(vozlisca[0].strip())
#        drugo_vozlisce = int(vozlisca[1].strip())
#        seznam_sosedov[prvo_vozlisce].append((drugo_vozlisce, 1))

#Najkrajša razdalja od 100 do 20.
#razdalja, pot = BFS_t(seznam_sosedov, 100, 20)
#print(razdalja)

if __name__ == "__main__":
    G = [
        [(1,1.5), (5,2)],
        [(3, 1), (4, 1.2), (5, 0.3)],
        [(4,1), (5, 0.8)],
        [(5,1), (2, 1.5)],
        [(4,1), (5, 0.8)],
        [(0, 1), (1,0.5), (4, 2)]
    ]
    s = 0
    t = 4
    razdalja, pot = BFS_t(G, s, t)

    print(razdalja)
    print(pot)