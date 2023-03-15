from functools import lru_cache
import matplotlib.pyplot as plt
import time
import math

# Časovna zahtevnost O(n*W)

def optimalni_tovor(predmeti, W):
    @lru_cache(maxsize=None)
    def najboljsi(i, W):
        if W < 0:
            return float("-inf")
        if W == 0 or i == 0:
            return 0
        return max(najboljsi(i-1,W), najboljsi(i-1,W-predmeti[i-1][1])+predmeti[i-1][0])
    return najboljsi(len(predmeti),W)


x1 = []
y1 = []

for i in range(2,30,2):
    predmeti = [(2,3) for _ in range(i*10)]
    volumen = 14*i
    skupaj=0
    for _ in range(100):
        zacetek = time.time()
        optimalni_tovor(predmeti,volumen)
        konec = time.time()
        skupaj+=konec-zacetek
    x1.append(len(predmeti))
    y1.append(skupaj/100)


x2 = []
y2 = []

for i in range(2,50,3):
    predmeti = [(2,3) for _ in range(i*10)]
    volumen = 14*math.log(i)
    skupaj=0
    for _ in range(100):
        zacetek = time.time()
        optimalni_tovor(predmeti,volumen)
        konec = time.time()
        skupaj+=konec-zacetek
    x2.append(len(predmeti))
    y2.append(skupaj/100)

x3 = []
y3 = []


for i in range(2,50,3):
    predmeti = [(2,3) for _ in range(i*10)]
    volumen = 35
    skupaj=0
    for _ in range(100):
        zacetek = time.time()
        optimalni_tovor(predmeti,volumen)
        konec = time.time()
        skupaj+=konec-zacetek
    x3.append(len(predmeti))
    y3.append(skupaj/100)
    
    
plt.plot(x3,y3,label = "st. predmetov: lin\n volumen: konst.")
plt.plot(x2,y2,label = "st. predmetov: lin\n volumen: log.")
plt.plot(x1,y1,label = "st. predmetov: lin\n volumen: lin.")

plt.title("Časovna zahtevnost\nRazlično naraščanje parametrov")
plt.legend()
# plt.savefig("cas_zahtevnost.pdf")
plt.show()

