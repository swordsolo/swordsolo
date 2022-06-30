def nextGreatElement(nums: list):
    n = len(nums)
    ans = [-1 for _ in range(n)]
    stack = []
    for i in range(n - 1, -1, -1):
        while len(stack) > 0 and stack[-1] <= nums[i]:
            stack.pop()
        if len(stack) == 0:
            ans[i] = -1
        else:
            ans[i] = stack[-1]
        stack.append(nums[i])
    return ans


nums = [2, 1, 2, 4, 3]


print(nextGreatElement(nums))

# O(n**2)
# def nextGreatElement(nums: list):
#     n = len(nums)
#     ans = [-1 for _ in range(n)]
#     for i in range(n):
#         for j in range(i+1, n):
#             if nums[j] > nums[i]:
#                 ans[i] = nums[j]
#                 break
#             else:
#                 ans[i] = -1
#     return ans
#
#
# nums = [2, 1, 2, 4, 3]
#
# print(nextGreatElement(nums))