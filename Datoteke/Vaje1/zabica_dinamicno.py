def zabica(mocvara):
    def skaci(i,e):
        if i >= len(mocvara):
            return 0
        if (i,e) in memo:
            return memo[(i,e)]
        nova_energija = e + mocvara[i] 
        min_skokov = min(skaci(i+k, nova_energija-k) for k in range(1, nova_energija+1))
        memo[(i,e)] = 1 + min_skokov
        return memo[(i,e)]

    memo = {}
    return skaci(0,0)