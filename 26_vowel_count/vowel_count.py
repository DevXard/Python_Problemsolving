def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    phrase = phrase.lower()
    result = {}
    voul = 'aeiou'
    for char in phrase:
        if char in voul and char not in result:
            result[char] = 1
        elif char in voul and char in result:
            result[char] += 1
    return result