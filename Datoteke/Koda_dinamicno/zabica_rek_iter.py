# iterativna resitev
def zabica(muhe):
    '''vrne minimalno potrebno število skokov'''
    n = len(muhe)
    dp = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[n][i]=0
        dp[n-1][i]=1
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            m = n
            e = j
            e += muhe[j] 
            for d in range(1,e+1):
                if i+d >= n:
                    m = 0
                else:
                    if e-d >= n:
                        m = 1
                    else:
                        m = min(m, dp[i+d][e-d])
                dp[i][j]=1+m
    return dp[0][0]

# resitev z rekurzijo
def zabica(mocvara):
    '''vrne minimalno potrebno število skokov'''
    def skaci(i,e):
        if i >= len(mocvara):
            return 0
        if (i,e) in memo:
            return memo[(i,e)]
        nova_energija = e + mocvara[i]
        min_skokov = min(skaci(i+k, nova_energija-k) for k in range(1,nova_energija+1))
        memo[(i,e)] = 1 + min_skokov
        return memo[(i,e)]
    memo = {}
    return skaci(0,0)