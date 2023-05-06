import random

def gen_graf(N):
    '''Funkcija konstruira nov graf, ki vsebuje le vozlišča od 0 do N.'''
    graf = []
    for vozl in range(N + 1):
        tab = []  # tabela sosedov i-tega vozlisca
        for _ in range(random.randint(1,N+1)):  #Vsako vozlisce bo imelo vsaj enega soseda.
            tab.append((random.randint(0,N+1), random.randint(0,N+1)))
        graf.append(tab)
    return graf

def txt(graf):
    '''Podatke o grafu shranimo v txt datoteko.'''
    with open('podatki_graf.txt', 'w') as dat:
        for i, sosedje in enumerate(graf):
            for sosed in sosedje:
                dat.write('{} {} {}\n'.format(i, sosed[0], sosed[1]))

txt(gen_graf(40))