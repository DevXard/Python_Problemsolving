def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    arr_of_chars = []
    for char in phrase:
        if char.islower() and char.lower() == to_swap.lower():
            arr_of_chars.append(char.upper())
        elif char.isupper() and char.lower() == to_swap.lower():
            arr_of_chars.append(char.lower())
        else:
            arr_of_chars.append(char)
    return ''.join(arr_of_chars)