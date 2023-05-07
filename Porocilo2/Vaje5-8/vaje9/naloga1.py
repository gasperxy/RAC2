import random

N = 1000

# Ustvari prazen graf
graf = [[] for _ in range(N)]

# Dodaj povezave z naključnimi utežmi
for i in range(N):
    for j in range(N):
        if i != j:
            utez = random.randint(1, 10) # naključna utež
            graf[i].append((j, utez))

# Shranimo graf v datoteko
with open('graf.txt', 'w') as f:
    for i in range(N):
        for j, utez in graf[i]:
            f.write(f"{i} {j} {utez}\n")
        
print("Done")