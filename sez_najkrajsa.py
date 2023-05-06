from podatki import podatki, UstvariGraf
from djikstra import djikstra

def najkrajsa_poti(s, t, drevo):
    '''Funkcija sprejme začetno vozlišče s ,končno vozlišče t
        ter drevo najkrajših poti ter vrne najkrajšo pot med njima v obliki seznama.'''
    seznam = [t]
    v = drevo[t]
    while v != s:
        seznam.append(v)
        v = drevo[v]
    seznam.append(s)
    return seznam

n = podatki()[0]
sez = podatki()[1]
G = UstvariGraf(n, sez)
razdalje, poti = djikstra(G, 100)

pot = najkrajsa_poti(100, 100000, poti)
print(pot)