# Konstruirajte nov graf, ki vsebuje le vozlišča od 0 do N.
# Vsaki povezavi določite neko pozitivno utež (lahko čisto naključno) in zadevo shranite v novo .txt datoteko.
# Vrstice naj bodo oblike u v w(u,v), kjer je (u, v) povezava in w(u, v) in njena utež.
import random
def nov_graf(n):
    E = set()
    with open('nov_graf.txt', 'w') as f:
        for i in range(n):
            u = i
            for _ in range(min(n, random.randint(1, 10))):
                v = random.randint(0, n - 1)
                while u == v:
                    v = random.randint(0, n - 1)
                w = random.randint(1, 10)
                if (u, v) in E:
                    continue
                E.add((u, v))
                f.write(f"{u}\t{v}\t{w}\n")

if __name__ == "__main__":
    nov_graf(100)