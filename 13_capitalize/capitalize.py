def capitalize(phrase):
    if not phrase:
        return ""
    return phrase[0].upper() + phrase[1:]
    # """Capitalize first letter of first word of phrase.
    #
    #     >>> capitalize('python')
    #     'Python'
    #
    #     >>> capitalize('only first word')
    #     'Only first word'
    # """