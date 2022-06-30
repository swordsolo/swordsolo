def coinChange(coins: list[int], amount: int):
    memo = dict()

    def dp(n):
        if n in memo: return memo[n]
        if n == 0: return 0
        if n < 0: return -1
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1: continue
            res = min(res, 1 + subproblem)
        memo[n] = res if res != float('INF') else -1
        return memo[n]

    return dp(amount)


num = coinChange([1, 2, 5], 90)
print(num)
