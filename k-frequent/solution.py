def solution(nums: list[int], k: int) -> list[int]:
    """
    Given an integer array nums and an integer k,
    return the k most frequent elements.
    You may return the answer in any order.
    """
    # get count of each item
    counter = {}
    for item in nums:
        counter[item] = counter.setdefault(item, 0) + 1

    # sort the counter with count as key in descending order
    result = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    # convert it to a list of keys
    result = list(dict(result).keys())

    # get the first k elements
    result = result[:k]

    return result
