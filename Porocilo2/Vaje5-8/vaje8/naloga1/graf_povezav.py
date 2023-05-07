import djikstra as djikstra

#Podatkovna struktura grafa
seznam_sosedov = [[] for line in open("roadNet-TX.txt") if line[0] != "#" or line != "" ]
with open("roadNet-TX.txt", "r") as f:
    for line in f:
        if line[0] == "#" or line == "":
             continue
        vozlisca = line.split("\t")
        prvo_vozlisce = int(vozlisca[0].strip())
        drugo_vozlisce = int(vozlisca[1].strip())
        seznam_sosedov[prvo_vozlisce].append((drugo_vozlisce, 1))
        
#Najkrajša razdalja od 100 do vseh ostalih
#razdalje, poti = djikstra.djikstra(seznam_sosedov, 100)
#print(razdalje)

#Najkrajša razdalja od 100 do 100000
#print(razdalje[100000])

#Najbolj oddaljeno vozlišče od 100
#print(razdalje.index(max(razdalje)))

#Število dosegljivih vozlišč od 100
#print(len(razdalje))