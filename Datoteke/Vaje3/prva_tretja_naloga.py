from functools import lru_cache

def optimalni_tovor(predmeti, W):
    '''Vrne največjo skupno ceno predmetov, ki jih lahko trgovec natovori na letalo z maksimalno nosilnostjo `W`.'''
    @lru_cache(maxsize=None)
    def najboljsi(i, W):
        # zaustavitvena pogoja
        if W < 0:
            # če nimamo prostora
            return float("-inf")
        if W == 0 or i == 0:
            # če nimamo več predmetov ali prostora
            return 0
        
        ne_vzamemo = najboljsi(i-1,W)  # ne vzamemo i-tega predmeta, W se ne spremeni
        vzamemo = najboljsi(i-1,W-predmeti[i-1][1])+predmeti[i-1][0]  # vzamemo i-ti predmet, W se ustrezno zmanjša, vrednost se ustrezno poveča
        return max(ne_vzamemo, vzamemo)
    return najboljsi(len(predmeti),W)



# Testni primeri za prvo nalogo
print('Testni primeri za prvo nalogo:')
predmeti1 = [(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)]
nosilnost1 = 7

predmeti2 = [(11,6), (40,9), (16,4), (32,7), (45,6), (48,7), (9,5), (44,9)]
nosilnost2 = 110

predmeti3 = [(2,3), (4,4), (5,4), (1,2), (15,12)]
nosilnost3 = 6

print(optimalni_tovor(predmeti1, nosilnost1))  # 8
print(optimalni_tovor(predmeti2, nosilnost2))  # 245
print(optimalni_tovor(predmeti3, nosilnost3))  # 6
print('\n')

def optimalni_tovor_zaloga(predmeti, W):
    '''Vrne največjo skupno ceno predmetov, ki jih lahko trgovec natovori na letalo z maksimalno nosilnostjo `W`.
        Sedaj so predmeti predstavljeni kot trojice (vrednost, teža, zaloga). Istih predmetov je toliko, kolikor je njegove zaloge.'''
    # ustvarimo novo tabelo, v kateri so navedeni predmeti tako, da lahko kličemo fn. iz prve naloge 
    nova = [(el[0], el[1]) for el in predmeti for _ in range(el[2])]
    return optimalni_tovor(nova, W)


# Testni primeri za tretjo nalogo
print('Testni primeri za tretjo nalogo:')
predmeti1 = [(2,3, 1), (4,4, 2), (5,4, 4), (3,2, 3), (1,2, 3), (15, 12, 2)]
nosilnost1 = 7

predmeti2 = [(11,6,2), (40,9,3), (16,4,3), (32,7,2), (45,6,1), (48,7,2), (9,5,3), (44,9,2)]
nosilnost2 = 110

print(optimalni_tovor_zaloga(predmeti1, nosilnost1))  # 9
print(optimalni_tovor_zaloga(predmeti2, nosilnost2))  # 492

