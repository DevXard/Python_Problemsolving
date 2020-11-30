def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    a = [int(x) for x in str(num1)]
    b = [int(x) for x in str(num2)]

    a_friq = {}
    b_friq = {}
    for num in a:
        if num not in a_friq:
            a_friq[f'{num}'] = 1
        else:
            a_friq[f'{num}'] +=1

    for num in b:
        if num not in a_friq:
            b_friq[f'{num}'] = 1
        else:
            b_friq[f'{num}'] += 1
    # print(a_friq, b_friq)
    if a_friq == b_friq:
        return True
    else:
        return False