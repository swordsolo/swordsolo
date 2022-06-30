def subsets(nums: list):
    n = len(nums)
    res = [[]]
    for i in range(n):
        print(i)
        tmp = res
        print(tmp)
        for j in tmp:
            res = res + [j + [nums[i]]]
        print(res)


nums = [i for i in range(1,6)]

subsets(nums)
