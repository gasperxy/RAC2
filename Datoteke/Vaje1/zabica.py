import random

def zabica(mocvara):
    """Vrne najmanjše število skokov, da pridemo ven iz močvare.
        Problem reši z memoizacijo."""
    n = len(mocvara)
    def skok(i, e):
        if n == 0:
            return 0
        if n == 1:
            return 1
        if i > n:
            return 0
        if (i, e) in slovar:
            return slovar[(i, e)]
        tab = []
        for koliko_skok in range(1, e + 1):
            if i + koliko_skok < n:
                tab.append(skok(i + koliko_skok, e - koliko_skok + mocvara[i + koliko_skok]))
        if len(tab) <= 0:
            return 0
        naj = min(tab) + 1
        slovar[(i, e)] = naj
        return slovar[(i, e)]
    slovar = dict()
    return skok(0, mocvara[0])

def test_gen_sez(n):
    "Generira testni seznam dolžine n."
    return [random.randint(1, n // 2) for _ in range(n)]

if __name__ == "__main__":
    mocvara_1 = [2, 4, 1, 2, 1, 3, 1, 1, 5]
    mocvara_2 = [4, 1, 8, 2, 11, 1, 1, 1, 1, 1]
    mocvara_3 = test_gen_sez(10)
    print(zabica(mocvara_1) == 3)
    print(zabica(mocvara_2) == 2)
    print(mocvara_3)
    print(zabica(mocvara_3))