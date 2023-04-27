def topoSort(G):
    '''
        Funkcija vrne topološko ureditev grafa `G` kot seznam.
        Graf je podan kot seznam sosednosti.
    '''
    n = len(G)  # število vozlišč
    in_deq = [0]*n  # beleženje število povezav v i-to vozlišče
    # gremo čez vsa vozlišča
    for i in range(n):
        # gremo čez vse sosede
        for j in G[i]:
            # obstaja povezava od i do j
            # povezava, ki kaže v j-to vozlišče, zato j povečamo število povezav
            in_deq[j] += 1
    
    izvori = [i for i in range(n) if in_deq[i] == 0]  # tista vozlišča, ki niso sosedje nobenemu oz. ni povezave, ki bi šla v ta vozlišča
    rezultat = list()
    
    # ponavljamo dokler bomo imeli vsaj en izvor
    while izvori:
        izvor = izvori.pop()
        # vsem sosedom izvora odstranimo in_deq
        rezultat.append(izvor)
        for sosed in G[izvor]:
            in_deq[sosed] -= 1
            if in_deq[sosed] == 0:
                # postal je novi izvor, ker je ostal brez sosedov
                izvori.append(sosed)
    
    return rezultat


g1= []
g2 = [[1], []]
g3 = [[1, 2], [2], []]
g4 = [[1, 2], [3, 5], [1, 3], [5], [1], []]
g5 = [[1, 2], [3], [4], [2, 4, 5], [5], []]

print(topoSort(g1))
print(topoSort(g2))
print(topoSort(g3))
print(topoSort(g4))
print(topoSort(g5))
    


