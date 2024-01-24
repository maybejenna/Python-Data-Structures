def titleize(phrase):
    holding_phrase = phrase.lower().split(" ")
    titleize_words = []
    for word_item in holding_phrase:
        if word_item:
            titleize_word = word_item[0].upper() + word_item[1:]
            titleize_words.append(titleize_word)

    titleized_phrase = " ".join(titleize_words)
    return print(titleized_phrase)

    # Test the function
    print(titleize("this is a test phrase"))
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

titleize('this is awesome')
titleize('oNLy cAPITALIZe fIRSt')