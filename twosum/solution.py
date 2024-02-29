def solution1(nums: list[int], target: int):
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add
    up to target.
    """
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
            j += 1
        i += 1


def solution(nums: list[int], target: int):
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add
    up to target.
    """
    indexmap = {}
    for index, item in enumerate(nums):
        if (target - item) in indexmap:
            return [indexmap[target - item], index]
        else:
            indexmap[item] = index
