def single_letter_count(word, letter):
    counter = word.count(letter)
    return print(f'The count of {letter} in {word} is {counter}')
    # """How many times does letter appear in word (case-insensitively)?
    #
    #     >>> single_letter_count('Hello World', 'h')
    #     1
    #
    #     >>> single_letter_count('Hello World', 'z')
    #     0
    #
    #     >>> single_letter_count("Hello World", 'l')
    #     3
    # """

single_letter_count('Hello World', 'h')
single_letter_count('Hello World', 'z')
single_letter_count("Hello World", 'l')