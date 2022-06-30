def knapsack(W: int, N: int, wt: list[int], val: list[int]):
    dp = [[0 for _ in range(W + 2)] for _ in range(N + 2)]
    for i in range(1, N + 1):
        for w in range(1, W + 1):
            if w - wt[i - 1] < 0:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w - wt[i - 1]] + val[i - 1], dp[i - 1][w])
    return dp[N][W]


print(knapsack(4, 3, [2, 1, 3], [4, 2, 3]))
