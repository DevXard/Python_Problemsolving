def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    # check if the words length is longer then n
    # and check if the length is biger or equal then 3
    # if so get rid of last 3 chars and add dots
    if len(phrase) >= n and n > 2:
        new_length = phrase[:n:]
        new_phrase = new_length[:-3:]
        return f"{new_phrase}..."
    elif n < 3:
        return 'Truncation must be at least 3 characters.'
    elif n > 3:
        return phrase
        