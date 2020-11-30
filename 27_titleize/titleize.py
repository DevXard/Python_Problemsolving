def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    phrase = phrase.lower()
    result = []
    split_words = phrase.split()
    for word in split_words:
        new_word = word.capitalize()
        result.append(new_word)
    return ' '.join(result)