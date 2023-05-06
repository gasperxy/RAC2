def pot_s_t(poti, s, t):
    """
    Skonstruira pot med s in t.
    """
    pot = []
    pot.append(t)
    pred = poti[t]
    while pred != s:
        pot.append(pred)
        pred = poti[pred]
    pot.append(s)
    return pot