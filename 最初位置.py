n=50
list=[1 for _ in range(n)]
print(list)
m=2
while sum(list)!=1:
    for i in range(int(n / m)):
        list[int(m * (i + 0.5) - 1)] = 0
    m*=2
    print(list)


print(list)
