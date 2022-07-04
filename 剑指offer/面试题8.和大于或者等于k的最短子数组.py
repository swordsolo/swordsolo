# def minSubArrayLen(nums,k):
#     n=len(nums)
#     for i in range(2,n+1):
#         for j in range(n-i+1):
#             if sum(nums[j:j+i])>=k:
#                 return i
#     return 0


def minSubArrayLen(nums,k):
    n=len(nums)
    left=0
    sum=0
    minLen=n+1
    for right in range(n):
        sum+=nums[right]
        while left<right and sum>=k:
            minLen=min(minLen,right-left+1)
            sum-=nums[left]
            left+=1
    if minLen==n+1:
        return 0
    else:
        return minLen

nums=[5,1,4,3]

print(minSubArrayLen(nums,5))