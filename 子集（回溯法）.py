res = [[]]


def subsets(nums: list):
    track = []
    backtrack(nums, 0, track)
    return res


def backtrack(nums: list, start: int, track: list):

    for i in range(start, len(nums)):
        track.append(nums[i])
        res.append(track[::])
        backtrack(nums, i + 1, track)
        track.pop()


nums = [1, 2, 3]

print(subsets(nums))