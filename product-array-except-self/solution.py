def solution(nums: list[int]) -> list[int]:
    """
    Given an integer array nums, return an array answer
    such that answer[i] is equal to the product of all
    the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed
    to fit in a 32-bit integer.
    """
    result = []

    # Bruteforce
    # for i in range(len(nums)):
    #     product = 1
    #     for j, multiplier in enumerate(nums):
    #         if i == j:
    #             continue
    #         product = product * multiplier
    #     result.append(product)

    n = len(nums)

    prefix = [nums[0]] + [1] * (n - 1)
    postfix = [1] * (n - 1) + [nums[-1]]
    for i in range(1, n):
        prefix[i] = prefix[i - 1] * nums[i]

    for i in range(n - 2, -1, -1):
        postfix[i] = postfix[i + 1] * nums[i]

    result = []
    for i in range(n):
        if i == 0:
            result.append(postfix[i + 1])
        elif i == n - 1:
            result.append(prefix[i - 1])
        else:
            result.append(prefix[i - 1] * postfix[i + 1])

    return result
