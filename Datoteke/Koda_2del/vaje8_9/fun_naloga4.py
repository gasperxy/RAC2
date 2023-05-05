
def pot(s, t, drevo):
    rez = []
    while t != s:
        rez.append(t)
        t = drevo[t]
    rez.append(s)
    return rez
