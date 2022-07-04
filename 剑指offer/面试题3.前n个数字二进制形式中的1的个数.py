def countBits(n):
    result=[0 for _ in range(n)]
    list=[bin(0)]
    for i in range(1,n):
        # result[i]=result[i>>1]+(i&1)
        result[i] = result[i & (i-1)] +1
        list.append(bin(i))

        # print(i,result)
    return result,list

print(countBits(32))