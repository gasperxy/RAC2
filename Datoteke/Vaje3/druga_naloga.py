def optimalni_predmeti(predmeti, W):
    '''Vrne seznam predmetov ki dosežejo največjo vrednost, če lahko na letalo natovorimo skupno težo največ `W`.'''
    predmeti = [(el[1],el[0]) for el in predmeti]
    n = len(predmeti)
    # ustvari matriko za hranjenje maksimalne vrednosti, ki je lahko posodobljena za vsak predmet
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]  # matrika velikosti (n+1)x(W+1)
    
    # grajenje matrike od spodaj navzgor
    for i in range(1, n + 1):  # z i gremo po vrsticah
        for j in range(1, W + 1):  # z j gremo po stolpciih
            # če trenutni predmet ustreza nahrbtniku
            if predmeti[i-1][0] <= j:
                # vzame največjo vrednost med tem, ali vzamemo predmet ali ne
                ne_vzamemo = dp[i-1][j]  # predmeta ne vzamemo
                vzamemo = dp[i-1][j-predmeti[i-1][0]] + predmeti[i-1][1]  # predmet vzamemo
                dp[i][j] = max(ne_vzamemo, vzamemo)
            else:
                # če trenutni predmet ne ustreza nahrbtniku, vzame vrednost prejšnjega predmeta
                dp[i][j] = dp[i-1][j]

    izbrani = list()
    j = W
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i-1][j]:
            izbrani.append(predmeti[i-1])
            j -= predmeti[i-1][0]

    # Vrne seznam izbranih predmetov
    izbrani = [(el[1],el[0]) for el in izbrani]
    return izbrani



# Testni primeri
predmeti1 = [(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)]
nosilnost1 = 7

predmeti2 = [(11,6), (40,9), (16,4), (32,7), (45,6), (48,7), (9,5), (44,9)]
nosilnost2 = 110

predmeti3 = [(2,3), (4,4), (5,4), (1,2), (15,12)]
nosilnost3 = 6

print(optimalni_predmeti(predmeti1, nosilnost1))  # [(3, 2), (5, 4)]
print(optimalni_predmeti(predmeti2, nosilnost2))  # [(44, 9), (9, 5), (48, 7), (45, 6), (32, 7), (16, 4), (40, 9), (11, 6)]
print(optimalni_predmeti(predmeti3, nosilnost3))  # [(1, 2), (5, 4)]


