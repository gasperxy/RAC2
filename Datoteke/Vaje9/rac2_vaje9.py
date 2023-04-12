# generiraj graf z vozlišči od 0 do N kot seznam sosednosti
import random
# 2. NALOGA

def generiraj_graf(n):
    '''
        Zgenerira in vrne graf kot seznam sosedov za število vozlišč od 0 do n.
        Torej n+1 vozlišč. Uteži so cela števila od 1 do 10.
    '''
    graf=list()
    for vozlisce in range(n+1):
        tab = list()  # tabela sosedov i-tega vozlisca
        for sosed in range(random.randint(1,n+1)):  # vsako vozlišče ima vsaj enega soseda
            tab.append((random.randint(0,n), random.randint(1,10)))  # (sosed, utež)
        graf.append(tab)
    return graf


def zapisi_txt(ime, graf):
    '''
        Zapiše graf v txt datoteko pod imenom ime.txt. Vrstice
        so v obliki `u v w(u,v)`, kjer je (u,v) povezava in w(u,v) njena utež.
        u je začetno in v končno vozlišče povezave.
    '''
    with open(ime + '.txt', 'w') as dat:
        for ind, sosedje in enumerate(graf):
            for sosed in sosedje:
                vrstica = '{} {} {}\n'
                dat.write(vrstica.format(ind, sosed[0], sosed[1]))


g1 = generiraj_graf(49)  # 50 vozlišč = 0, 1, 2,... 49
zapisi_txt('graf_g1', g1)



