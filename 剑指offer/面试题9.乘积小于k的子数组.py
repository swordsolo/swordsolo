def subArrayProductLessThanK(nums,k):
    n=len(nums)
    print(nums)
    product=1
    left=0
    # right=0
    list=[]
    for right in range(n):
        product=nums[right]
        left=right
        while left>=0 and product<k:
            list.append(nums[left:right+1])
            left-=1
            product*=nums[left]
    return list,len(list)

nums=[10,5,2,6]
print(subArrayProductLessThanK(nums,100))
