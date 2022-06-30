def dailyTemperature(T: list):
    n = len(T)
    s = []
    ans = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        while len(s) != 0 and T[s[-1]] <= T[i]:
            s.pop()
        if len(s) == 0:
            ans[i] = 0
        else:
            ans[i] = s[-1] - i
        s.append(i)
    return ans


T = [73, 74, 75, 72, 69, 73, 76, 73]
print(dailyTemperature(T))