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
            for _ in range(min(N, random.randint(1, 10))):
                v = random.randint(0, N) # ustvarimo vozlišče v katerega gre u
                while u == v:
                    v = random.randint(0, N)
                w = random.randint(1, 10) # določimo ceno te povezave
                if (u, v) in povezave:
                    continue
                povezave.add((u, v))
                datoteka.write(f"{u}\t{v}\t{w}\n")

if __name__ == "__main__":
    pass