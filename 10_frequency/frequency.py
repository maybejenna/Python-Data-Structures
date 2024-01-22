def frequency(lst, search_term):
    freq = 0
    for item in lst:
        if item == search_term:
            freq += 1
    return freq
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

print (frequency([1, 4, 3, 4, 4], 4))
print (frequency([1, 4, 3], 7))