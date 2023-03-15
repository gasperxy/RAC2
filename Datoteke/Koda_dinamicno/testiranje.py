from functools import lru_cache
from termcolor import colored


def optimalni_tovor(predmeti, W):
    @lru_cache(maxsize=None)
    def najboljsi(i, W):
        if W < 0:
            return float("-inf")
        if W == 0 or i == 0:
            return 0
        return max(najboljsi(i-1, W), najboljsi(i-1, W-predmeti[i-1][1])+predmeti[i-1][0])
    return najboljsi(len(predmeti), W)


# testni primeri
testi = [
    {'vnos': {'skupaj': 3, "predmeti": [(10,10)]}, "rezultat":0},
    {'vnos': {'skupaj': 3, "predmeti": []}, "rezultat":0},
    {'vnos': {'skupaj': 10, "predmeti":[(20, 1), (5, 2), (10, 3), (40, 8), (15, 7), (25, 4)]}, "rezultat":60},
    {'vnos': {'skupaj': 40, "predmeti":[(10, 30), (20, 10), (30, 40), (40, 20)]}, "rezultat":60},
    {'vnos': {'skupaj': 3, "predmeti":[(1, 4), (2, 5), (3, 6)]}, "rezultat":0},
    {'vnos': {'skupaj': 170, "predmeti": [(422, 41), (525, 50), (511, 49), (593, 59), (546, 55), (564, 57), (617, 60)]}, "rezultat":1735},
    {'vnos': {'skupaj': 15, "predmeti": [(2, 4), (3, 5), (1, 1), (5, 3), (4, 2), (7, 5)]}, "rezultat":19},
    {'vnos': {'skupaj': 269, "predmeti": [(55, 95), (10, 4), (47, 60), (5, 32), (4, 23), (50, 72), (8, 80), (61, 62), (85, 65), (87, 46)]}, "rezultat":295},
    {'vnos': {'skupaj': 878, "predmeti": [(44, 92), (46, 4), (90, 43), (72, 83), (91, 84), (40, 68), (75, 92), (35, 82), (8, 6), (54, 44), (78, 32), (40, 18), (77, 56), (15, 83), (61, 25), (17, 96), (75, 70), (29, 48), (75, 14), (63, 58)]}, "rezultat":1024},
    {'vnos': {'skupaj': 3050, "predmeti": [(i+i % 20, i) for i in range(5, 200, 5)]}, "rezultat":3340},
    ]
n = len(testi)
pravilno = 0
for test in testi:
    vnos = test["vnos"]
    rezultat = test["rezultat"]
    if optimalni_tovor(vnos["predmeti"], vnos["skupaj"]) == rezultat:
        pravilno += 1/n
        print(colored(f"=== {round(pravilno*100,1)}% ===",'green'))
    else:
        print(colored("=== FAIL  ===",'red'))
