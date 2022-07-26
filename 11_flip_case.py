def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swapped_case = []

    for letter in phrase:
        if letter.lower() == to_swap.lower():
            swapped_case.append(letter.swapcase())
        else:
            swapped_case.append(letter)

    return ''.join(swapped_case)
