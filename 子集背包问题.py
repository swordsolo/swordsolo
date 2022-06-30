def canPatition(nums: list[int]):
    n = len(nums)
    sum = 0
    for num in nums:
        sum += num
    if sum % 2 != 0:
        return False
    sum = sum // 2
    dp = [[False for _ in range(sum + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j - nums[i - 1] < 0:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j] | dp[i - 1][j - nums[i - 1]]
    return dp[n][sum]


nums = [1, 5, 11, 5,2]

print(canPatition(nums))
