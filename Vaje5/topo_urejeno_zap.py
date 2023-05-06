def topo_sort(G):
    '''Vrne topološko ureditev grafa `G`, ki je podan kot seznam sosednosti.'''
    n = len(G)  
    in_deq = [0]*n  # in_deq[i] --- št povezav, ki kaže v i
    for i in range(n):  #vozlišča
        for j in G[i]:    #sosedi
            in_deq[j] += 1
    
    izvori = [i for i in range(n) if in_deq[i] == 0]  #vozlišča, ki niso sosedi nobenemu
    rezultat = []
    
    while izvori:
        izvor = izvori.pop()
        rezultat.append(izvor)
        for sosed in G[izvor]:
            in_deq[sosed] -= 1
            if in_deq[sosed] == 0:
                izvori.append(sosed)  #nima vec sosedov, zato je nov izvor
    
    return rezultat
