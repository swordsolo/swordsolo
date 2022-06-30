n=50
m=2
list=[_+1 for _ in range(n)]
for i in range(int(n / m)):
    list[int(m * (i + 0.5) - 1)] = 0
print(list)


