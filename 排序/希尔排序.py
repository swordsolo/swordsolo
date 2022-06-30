def shell_sort(list):
    n=len(list)
    step=2
    group=n//step
    while group>0:
        for i in range(group):
            j=i+group
            while j<n:
                k=j-group
                key=list[j]
                while k>=0:
                    if list[k]>key:
                        list[k+group]=list[k]
                        list[k]=key
                    k-=group
                j+=group
        group//=step
    return list

if __name__=="__main__":
    list=[9,8,7,6,5,4,3,2,1]
    print(shell_sort(list))
