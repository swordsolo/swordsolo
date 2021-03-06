def superEggDrop(K: int, N: int):
    memo = dict()

    def dp(K, N) -> int:
        # base case
        if K == 1: return N
        if N == 0: return 0
        if (K, N) in memo:
            return memo[(K, N)]
        res = float('INF')
        for i in range(1, N + 1):
            res = min(res , max(dp(K, N - i), dp(K - 1, i - 1)) + 1)

            memo[(K, N)] = res
        return memo[(K, N)]

    return dp(K, N)


print(superEggDrop(200,100))
