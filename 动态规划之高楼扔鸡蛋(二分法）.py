def superEggDrop(K: int, N: int):
    memo = dict()

    def dp(K, N) -> int:
        # base case
        if K == 1: return N
        if N == 0: return 0
        if (K, N) in memo:
            return memo[(K, N)]
        res = float('INF')
        lo = 1
        hi = N
        while lo <= hi:
            mid = (lo + hi) // 2
            broken = dp(K - 1, mid - 1)
            unbroken = dp(K, N - mid)
            if broken > unbroken:
                hi = mid - 1
                res = min(res, broken + 1)
            else:
                lo = mid + 1
                res = min(res, unbroken + 1)
        memo[(K, N)] = res
        return res

    return dp(K, N)


print(superEggDrop(3, 100))
