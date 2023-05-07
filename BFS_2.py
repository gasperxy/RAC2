def BFS_2(G, u, t):
    '''Funkcija vrne seznam poti od vozlisca u do vozlišča t v grafu G'''
    n = len(G)
    razdalje = [0]*n
    obiskani = [False]*n
    q = ([(u,0,u)]) #začnemo v u, razdlaja je na začetku 0
    poti =[None]*n
    while q: #dokler vrsta ni prazna
        trenutni, razdalja, prejsni = q.pop(0)
        if obiskani[trenutni]:
            continue #soseda smo že obiskali

        if trenutni == t:
            break 
        #v primeru da smo prišli do našega željenga končnega vozlišča t zaključimo s to zanko
        obiskani[trenutni] = True
        razdalje[trenutni] = razdalja
        poti[trenutni] = prejsni
        for sosed, teza in G[trenutni]:
            if not obiskani[sosed]:
                q.append((sosed, razdalja +1, trenutni)) #v vrsto dodamo soseda,razdalji prištejemo ena
    return razdalje, poti