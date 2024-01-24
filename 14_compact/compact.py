def compact(lst):
    compact_lst = []
    for item in lst:
        if item:
            compact_lst.append(item)
    return compact_lst
    # """Return a copy of lst with non-true elements removed.
    #
    #     >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
    #     [1, 2, 'All done']
    # """

print (compact([0, 1, 2, '', [], False, (), None, 'All done']))