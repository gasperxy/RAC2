from podatki import podatki, UstvariGraf

def bfs_iskanjeOduDot(G, u, t):
    '''Implemantacija BFS algoritma od vozlišča u do vozlišča t
       Funkcija vrne razdaljo in seznam ocetov'''
    if u == t: #Vozlisci se ujemata
        return 0, []
    n = len(G)
    d = [-1]*n
    obiskani = [False]*n
    q = [(u,0,u)] #Vozlišča in njihovi starši
    vrsta = [(u,0,u)]
    poti = []
    while q:
        trenutni, razdalja, prej = q.pop(0)
        if obiskani[trenutni]:
            continue
            
        obiskani[trenutni] = True
        for sosed in G[trenutni]:
            if razdalja == 0 and sosed == t: #Direktni sosed
                return 1, [sosed, u]
            if not obiskani[sosed]:
                q += [(sosed, razdalja + 1, trenutni)]
                vrsta += [(sosed, razdalja, trenutni)]
            if sosed == t:
                poti.append(t)
                poti.append(trenutni)
                while True: #Ustavimo se ko pridemo do vozlisca t.
                    for element in vrsta:
                        if element[0] == trenutni:
                            prej = element[2]
                            if prej == u:
                                poti.append(u)
                                return razdalja + 1, poti
                            poti.append(prej)
                            trenutni = prej
# Glavni program
G2_neutezen = [
     [1, 5],
     [3, 4, 5],
     [4, 5],
     [5, 2],
     [4, 5],
     [0, 1, 4]
 ]
print(bfs_iskanjeOduDot(G2_neutezen, 0, 2))    