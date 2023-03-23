def stevilo_poti_iterativno(n, m, mine):
    '''Iterativna verzija algoritma za nalogo Minsko polje.
    '''
    # vse točke iz tabele mine damo v množico, zaradi nadaljnega hitrejšega iskanja točk
    # tako se le enkrat sprehodimo po tabeli
    mnozica_min = set(mine)
    # pripravimo si matriko, v kateri hranimo št. možnih poti do nekega polja
    A = [[0]*m for _ in range(n)]
    
    # levi in zgornji rob nastavimo na 1 vsa tista polja, ki nimajo min
    # saj do njih se da priti le po eni možnosti
    for levi in range(n):
        if (levi, 0) not in mnozica_min:
            A[levi][0] = 1
    
    for zgornji in range(m):
        if (0, zgornji) not in mnozica_min:
            A[0][zgornji] = 1
    
    for j in range(1, m):
        for i in range(1, n):
            if (i, j) not in mnozica_min:
                # polje je varno
                A[i][j] = A[i][j-1] + A[i-1][j]
            else:
                # polje ima mino
                continue
        
    return A[n-1][m-1]
    


# testni podatki za funkcijo
mine1 = []
mine2 = [(1, 2), (3, 2)]

print(stevilo_poti_iterativno(5, 4, mine1))  # 35
print(stevilo_poti_iterativno(5, 4, mine2))  # 9
