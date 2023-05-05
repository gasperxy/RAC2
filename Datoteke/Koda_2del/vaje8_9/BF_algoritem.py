def BF(seznam, s):
    n = len(seznam)
    raz = [float("inf")]*n
    prej = [None] * n
    raz[s] = 0

    for _ in range(n):
        for i in range(n):
            for j in range(len(seznam[i])):
                do, utez = seznam[i][j]
                trenutna = raz[i] + utez
                if trenutna < raz[do]:
                    raz[do] = trenutna
                    prej[do] = i

    for i in range(n):
        for j in range(len(seznam[i])):
            do, utez = seznam[i][j]
            if raz[i] + utez < raz[do]:
                print("Neg cikel")
    return raz, prej


def BF_ustavitev(seznam, s):
    n = len(seznam)
    raz = [float("inf")]*n
    prej = [None] * n
    raz[s] = 0
    for _ in range(n):
        sprememba = False
        for i in range(n):
            for j in range(len(seznam[i])):
                do, utez = seznam[i][j]
                trenutna = raz[i] + utez
                if trenutna < raz[do]:
                    sprememba = True
                    raz[do] = trenutna
                    prej[do] = i
        if not sprememba:
            break

    for i in range(n):
        for j in range(len(seznam[i])):
            do, utez = seznam[i][j]
            if raz[i] + utez < raz[do]:
                print("Neg cikel")
    return raz, prej


# aa = [[(1, 6), (2, 5), (3, 5)], [(4, -1)], [(1, -2), (4, 1)],
#       [(2, -2), (5, -1)], [(6, 3)], [(6, 3)], []]
# print(BF(aa, 0))
