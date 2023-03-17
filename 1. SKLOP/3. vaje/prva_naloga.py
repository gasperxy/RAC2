from functools import lru_cache


def optimalni_tovor(predmeti, W):
    @lru_cache(maxsize=None)
    def pomozna(i, W):
        if W < 0:
            # če nimamo prostora
            return float("-inf")
        if W == 0 or i == 0:
            # če nimamo več predmetov ali prostora
            return 0
        ne_vzamemo = pomozna(i-1,W)  # ne vzamemo i-tega predmeta, W se ne spremeni
        vzamemo = pomozna(i - 1, W - predmeti[i-1][1]) + predmeti[i-1][0]  # vzamemo i-ti predmet, W se ustrezno zmanjša, vrednost se ustrezno poveča
        return max(ne_vzamemo, vzamemo)
    return pomozna(len(predmeti),W)


# Testni primeri
test1 = print(optimalni_tovor([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 7))
test2 = print(optimalni_tovor([], 7))
test3 = print(optimalni_tovor([(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)], 0))
