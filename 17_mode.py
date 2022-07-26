def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """

    frequency = {}

    for num in nums:
        # if frequency.get(num):
        #     frequency[num] += 1
        # else:
        #     frequency[num] = 1
        frequency[num] = (frequency.get(num) or 0) + 1

    return max(frequency, key = frequency.get)

    # highest_count = {num: nums.count(num) for num in nums}
    # return max(highest_count)

    #.count is O(n)
    #use max with 2nd arg