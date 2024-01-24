def list_check(lst):
    is_list = True
    for item in lst:
        if isinstance(item, list):
            is_list = True
        else:
            is_list = False

    return  print(is_list)
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """
list_check([[1], [2, 3]])
list_check([[1], "nope"])