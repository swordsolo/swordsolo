def superEggDrop(k: int, n: int):
    dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
    m = 0
    lo, hi = 1, n
    while lo < hi:
        mid = (lo + hi) // 2
        # if dp[k][mid] == n:
        #     return mid
        if dp[k][mid] < n:
            lo = mid + 1
        if dp[k][mid] > n:
            hi = mid - 1
    # while dp[k][m] < n:
    #     m += 1
    #     for i in range(k + 1):
    #         dp[i][m] = dp[i - 1][m - 1] + dp[i][m - 1] + 1
        for i in range(k + 1):
            dp[i][mid] = dp[i - 1][mid - 1] + dp[i][mid - 1] + 1
    return m


print(superEggDrop(7, 10000))
