list=[0,1,0,1,0,1,100,100,2]
nums=[]
for i in list:
    if i not in nums:
        nums.append(i)
n=len(nums)
l=[0 for _ in range(n)]
for i in list:
      for j in range(n):
          if i==nums[j]:
              l[j]+=1
index=0
for i in range(n):
    if l[i]==1:
        index=i

print(nums[index])