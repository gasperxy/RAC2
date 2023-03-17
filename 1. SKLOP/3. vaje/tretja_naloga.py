from prva_naloga import optimalni_tovor
def optimalni_tovor_zaloga(predmeti, W):
    nova = [(el[0], el[1]) for el in predmeti for _ in range(el[2])]
    return optimalni_tovor(nova, W)

test1 = print(optimalni_tovor_zaloga([(2,3, 1), (4,4, 2), (5,4, 4), (3,2, 3), (1,2, 3), (15, 12, 2)], 7))