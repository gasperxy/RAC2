from djikstra import *
from naloga1 import * 

def najkrajsa_pot(s, t, poti):
    """
    Funkcija sprejme začetno vozlišče s, končno vozlišče t ter drevo 
    najkrajših poti kot seznam, vrne pa najkrajšo pot med vozliščema 
    v obliki seznama.
    """
    pot_do_t = [t]
    predhodnik = poti[t]
    # dokler predhodnik ni začetno vozlišče 
    # v seznam dodajamo vozlišča 
    while predhodnik != s:
        pot_do_t.append(predhodnik)
        predhodnik = poti[predhodnik]
    pot_do_t.append(s) 
    return pot_do_t

if __name__=="__main__":
    G = ustvari_graf("roadNet-TX.txt")
    d, poti = djikstra(G, 100)
    najkrajsa_pot = najkrajsa_pot(100, 100000, poti)
    # preverimo ali se skonstruirana pot ujema s dijkstrinim algoritmom
    # odštejemo -1 saj ima pot eno manj povezavo kot vozlišč
    print(len(najkrajsa_pot)-1 == d[100000])