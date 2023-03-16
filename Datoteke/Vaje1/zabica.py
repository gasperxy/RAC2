def zabica(mocvara):
    """Vrne najmanjše število skokov, da pridemo ven iz močvare.
        Problem reši z memoizacijo."""
    n = len(mocvara)
    def skok(i, e):
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