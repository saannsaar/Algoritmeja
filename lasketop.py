def numOfTopologicalSorts(n):
    MOD = 10**9 + 7
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for l in range(2, n+1):
        for i in range(n - l + 1):
            j = i + l - 1
            for k in range(i, j):
                dp[i][j] = (dp[i][j] + dp[i][k]) % MOD
    return sum(dp[i][i] for i in range(n)) % MOD

print(numOfTopologicalSorts(1000))