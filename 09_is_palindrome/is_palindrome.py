def is_palindrome(phrase):
    lower_phrase = phrase.lower()
    reverse = lower_phrase[::-1]
    if lower_phrase == reverse:
        return print("True")
    else:
        return print("False")
    #
    # """Is phrase a palindrome?
    #
    # Return True/False if phrase is a palindrome (same read backwards and
    # forwards).
    #
    #     >>> is_palindrome('tacocat')
    #     True
    #
    #     >>> is_palindrome('noon')
    #     True
    #
    #     >>> is_palindrome('robert')
    #     False
    #
    # Should ignore capitalization/spaces when deciding:
    #
    #     >>> is_palindrome('taco cat')
    #     True
    #
    #     >>> is_palindrome('Noon')
    #     True
    # """
is_palindrome('tacocat')
is_palindrome('noon')
is_palindrome('robert')
is_palindrome('TacoCat')
is_palindrome('Noon')
