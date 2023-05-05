from djikstra import djikstra

def naj():
    naj = 0
    with open('roadNet-TX.txt','r') as f:
            vrstice =f.readlines()
            veljavne = vrstice[4:]
            for vrstica in veljavne:
                trenutna = vrstica.strip().split("\t")
                od = int(trenutna[0])
                do = int(trenutna[1])
                if od > naj:
                    naj = od
    return naj
            


def omrezje(n):
    vse = [[] for _ in range(n+1)]
    with open('roadNet-TX.txt','r') as f:
        vrstice =f.readlines()
        veljavne = vrstice[4:]
        for vrstica in veljavne:
            trenutna = vrstica.strip().split("\t")
            od = int(trenutna[0])
            do = int(trenutna[1])
            vse[od].append((do,1))
    return vse


