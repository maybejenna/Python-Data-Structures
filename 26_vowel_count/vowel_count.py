def vowel_count(phrase):
    lower_phrase = phrase.lower()
    vowel_count = {
        "a": 0,
        "e":0,
        "i":0,
        "o":0,
        "u":0
    }
    for letter in lower_phrase:
        if letter in vowel_count:
            vowel_count[letter] += 1

    for vowel in list(vowel_count.keys()):
        if vowel_count[vowel] == 0:
            del vowel_count[vowel]

    return print(vowel_count)
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

vowel_count('rithm school')
vowel_count('HOW ARE YOU? i am great!')