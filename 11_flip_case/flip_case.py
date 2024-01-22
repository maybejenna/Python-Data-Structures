def flip_case(phrase, to_swap):
    def flip_case(phrase, to_swap):
        result = ""
        for letter in phrase:
            if letter.lower() == to_swap.lower():
                if letter.isupper():
                    result += letter.lower()
                else:
                    result += letter.upper()
            else:
                # If the letter does not match, keep it as is
                result += letter
        return result
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

print (flip_case('Aaaahhh', 'a'))
print (flip_case('Aaaahhh', 'A'))