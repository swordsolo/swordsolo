res = []

def permute(nums: list):
    track = []
    backtrack(nums, track)
    return res


def backtrack(nums: list, track: list):
    if len(track) == len(nums):
        res.append(track[::])
        return

    for i in range(len(nums)):
        if nums[i] in track:
            continue
        track.append(nums[i])
        backtrack(nums,track)
        track.pop()

nums=[1,2,3]

print(permute(nums))