def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    compact_list = []
    for el in lst:
        if bool(el):
            compact_list.append(el)
    return compact_list