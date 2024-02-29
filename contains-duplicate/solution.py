def solution(nums):
    """
    Does the given list of numbers, has any duplicates?
    """
    # Initialize a counter to store the occurences for each unique number
    counter = {}
    for item in nums:

        # If a number is already there in the counter, that means it is a duplicate
        if counter.get(item):
            return True
        else:
            # Store the number in the counter
            counter[item] = 1

    # No duplicates found
    return False
