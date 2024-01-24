def extract_full_names(people):
    names = [
        {'first': 'Ada', 'last': 'Lovelace'},
        {'first': 'Grace', 'last': 'Hopper'},
        ]

    full_name = []

    for person in people:
        full_name = person['first'] + ' ' + person['last']
        full_name.append(full_name)
    return full_name

    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names(names)
        ['Ada Lovelace', 'Grace Hopper']
    """