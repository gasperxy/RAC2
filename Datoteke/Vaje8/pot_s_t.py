from BFS_poti import *

def pot_s_t(s, t, drevo_najkrajsih):
    '''
        Vrne pot od vozlišča s do t na podlagi drevesa najkrajših poti od vozlišča s do vseh ostalih.
    '''
    sez = list()
    v = drevo_najkrajsih[t]
    sez.append(t)
    while v != s:
        sez.append(v)
        v = drevo_najkrajsih[v]
        
    sez.append(s)
    return sez


#razdalje, drevo = BFS_poti(G2_neutezen, 0)
#print(pot_s_t(0, 2, drevo))

    
    

