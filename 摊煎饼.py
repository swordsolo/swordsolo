res=[]
def pancakesort(cakes:list):
    sort(cakes,len(cakes))
    return res

def sort(cakes:list,n:int):
    if n==1:
        return
    maxcake=0
    maxcakeindex=0
    for i in range(n):
        if cakes[i]>maxcake:
            maxcake=cakes[i]
            maxcakeindex=i
    reverse(cakes,0,maxcakeindex)
    res.append(maxcakeindex+1)
    reverse(cakes,0,n-1)
    res.append(n)
    sort(cakes,n-1)

def reverse(arr:list,i:int,j:int):
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1

# cakes=[3,2,4,1]
cakes=[4,3,2,1]
print(pancakesort(cakes))-0