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
    greatest = None
    counter = 0
    for num in nums:
        if nums.count(num) > counter:
            greatest = num
            counter = nums.count(num)

    return greatest

    # highest_count = {num: nums.count(num) for num in nums}
    # return max(highest_count)