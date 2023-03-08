def najvecji_dobicek(zlato):
    '''Vrne največjo število kovancev, ki jih lahko dobi igralec ob predpostavki,
        da oba igrata optimalno.'''
    n = len(zlato)
    if n == 0:
        return 0
    elif n == 1:
        return zlato[0]
    
    def pomozna(tab):
        if len(tab) == 2:
            # imamo le dve košari, izberemo največjo
            return max(tab)
        
        # vzamemo prvo košaro, nasprotni igralec bo vzel večjo košaro na robu tabele tab[1:], to spustimo
        if tab[1] > tab[-1]:
            prva = tab[0] + pomozna(tab[2:])
        else:
            prva = tab[0] + pomozna(tab[1:-1])
            
        # vzamemo zadnjo košaro, nasprotni igralec bo vzel večjo košaro na robu tabele tab[:-1], to spustimo
        if tab[0] > tab[-2]:
            zadnji = tab[-1] + pomozna(tab[1:-1])
        else:
            zadnji = tab[-1] + pomozna(tab[:-2])
            
        return max(prva, zadnji)
        
    return pomozna(zlato)



# testni podatki za funkcijo
zlato1 = []
zlato2 = [15]
zlato3 = [15, 34]
zlato4 = [4, 6, 2, 3]

print(najvecji_dobicek(zlato1))  # 0
print(najvecji_dobicek(zlato2))  # 15
print(najvecji_dobicek(zlato3))  # 34
print(najvecji_dobicek(zlato4))  # 9

