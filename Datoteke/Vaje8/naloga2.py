from BFS import *

def ustvari_graf(datoteka):
    """
    Funkcija prejme ime tekstovne datoteke, ki vsebuje usmerjene povezave in iz nje 
    ustvari neutežen graf z usmerjenimi povezavami, predstavljen kot seznam sosednosti.
    """
    with open('Datoteke\\Vaje8\\' + datoteka, 'r') as datoteka:
        # prve 4 vrstice ne porebujemo, jih samo preberemo
        for _ in range(4):
            datoteka.readline()
        
        # napolnemo seznam povezav s povezavami iz datoteke roadNET-TX.txt
        sez_povezav = []
        for vrstica in datoteka:
            vrstica = vrstica.strip().split('\t')
            sez_povezav.append((int(vrstica[0]), int(vrstica[1])))

        # uredimo vozlišča po velikosti, da dobimo največje vozlišče, saj bo 
        # naš graf G, predstavljen kot seznam sosednosti, vseboval n+1 povezav
        sez_povezav.sort(key=lambda x: x[0], reverse=True)
        n = sez_povezav[0][0]

        # Ustvarimo seznam sosednosti, kjer so povezave usmerjene, uteži pa enake 1
        G = [[] for _ in range(n+1)]
        for povezava in sez_povezav:
            u = povezava[0]
            v = povezava[1]
            # Ker bomo uporabili BFS graf ne sme vsebovati uteži!!!
            # Tu je razlika v primerjavi z nalogo1
            G[u].append(v)
    return G

G = ustvari_graf("roadNet-TX.txt")

if __name__=="__main__":
    # d ... seznam najkrajših razdalj od vozlišča 100 do vseh ostalih
    # p ... drevo najkrajših poti od vozlišča 100 do vseh ostalih vozlišč
    d, p = BFS(G, 100)
    # print(d[:11])

    #==================================================================================
    # razdalja od vozlišča 100 do 100000
    # print(d[100000])
    # vozlišče zadnje na tej poti 
    # print(p[100000])

    #==================================================================================
    # katero vozlišče je najbolj oddaljeno od vozlišča 100
    # najvecja_razdalja = max(d)
    # najdaljsi = []
    # indeksi = []

    # for indeks, razdalja in enumerate(d):
    #     if najvecja_razdalja == razdalja:
    #         najdaljsi.append(razdalja)
    #         indeksi.append(indeks)
    # print(indeksi)
    # print(najdaljsi)

    #==================================================================================
    # koliko vozlišč je dosegljivih od vozlišča 100
    # print(len(G[100]))