def monotonic(nums: list, k: int):
    res = []
    window = []
    n = len(nums)
    for i in range(n):
        if i < k - 1:
            push(window, nums[i])
        else:
            push(window, nums[i])
            res.append(gmax(window))
            pop(window, nums[i - k + 1])
    return res

def push(window: list, n: int):
    while len(window) != 0 and window[-1] < n:
        window.pop()
    window.append(n)

def gmax(window: list):
    return window[0]


def pop(window: list, n: int):
    if n == window[0]:
        window.pop(0)


nums = [1, 3, -1, -3, 5, 3, 6, 7]

print(monotonic(nums, 3))
