def solution(strs: list[str]):
    """
    Given an array of strings strs, group the anagrams
    together. You can return the answer in any order.

    An Anagram is a word or phrase formed by rearranging
    the letters of a different word or phrase, typically
    using all the original letters exactly once.
    """
    output = {}
    found = set()
    for index, item in enumerate(strs):
        if index in found:
            continue

        sorted_item = "".join(sorted(item))

        if sorted_item in output:
            output[sorted_item].append(item)
        else:
            output[sorted_item] = [item]

        found.add(index)

        for i in range(index + 1, len(strs)):
            if i in found:
                continue
            if sorted_item == "".join(sorted(strs[i])):
                output[sorted_item].append(strs[i])
                found.add(i)
            else:
                i += 1

    result = [value for value in output.values()]

    return result


def compare_output(result, output) -> bool:
    """ """
    result = [sorted(item) for item in result]
    output = [sorted(item) for item in output]
    return sorted(result) == sorted(output)
