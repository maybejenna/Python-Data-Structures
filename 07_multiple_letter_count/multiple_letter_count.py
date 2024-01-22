def multiple_letter_count(phrase):
    return print ({letter: phrase.count(letter) for letter in set(phrase)})

    # """Return dict of {ltr: frequency} from phrase.
    #
    #     >>> multiple_letter_count('yay')
    #     {'y': 2, 'a': 1}
    #
    #     >>> multiple_letter_count('Yay')
    #     {'Y': 1, 'a': 1, 'y': 1}
    # """

multiple_letter_count('yay')
multiple_letter_count('Yay')
multiple_letter_count('jenna')