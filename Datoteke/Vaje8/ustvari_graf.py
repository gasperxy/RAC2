import random

def ustvari_graf(N):
    """
    Funkcija sprejme število N, ki predstavlja število vozlišč. Ustvari novo .txt 
    datoteko na katero zapiše nov graf z vozlišči od 0 do N. Vozlišča so oblike 
    (u, v) w(u, v), kjer je (u, v) povezava in w(u, v) je njena utež.
    """
    povezave = set()
    with open('ustvari_graf.txt', 'w') as datoteka:
        for u in range(N+1):
            st_povezav = random.randint(1, 10) 
            for _ in range(st_povezav):
                if st_povezav > N: # povezav do nekega vozlišča je več kolikor povezav v grafu
                    break
                v = random.randint(0, N) # ustvarimo vozlišče v katerega gre u
                if u == v:
                    continue
                w = random.randint(1, 10) # določimo ceno te povezave
                if (u, v) in povezave:
                    continue
                povezave.add((u, v))
                datoteka.write(f"{u}\t{v}\t{w}\n")

if __name__ == "__main__":
    #ustvari_graf(2000)
    pass