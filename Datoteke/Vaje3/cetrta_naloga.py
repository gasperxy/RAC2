def neomejena_zaloga(predmeti, W):
    def pomozna(W, n, val, wt):
        dp = [0 for i in range(W+1)]
        for i in range(W+1):
            for j in range(n):
                if (wt[j] <= i):
                    dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
        return dp[W]
    return pomozna(W, len(predmeti), [el[0] for el in predmeti], [el[1] for el in predmeti])


# Testni primeri
predmeti1 = [(2,3), (4,4), (5,4), (3,2), (1,2), (15, 12)]
nahrbtnik1 = 23

print(neomejena_zaloga(predmeti1, nahrbtnik1))  # 33

