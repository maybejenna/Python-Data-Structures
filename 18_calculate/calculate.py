def calculate(operation, a, b, make_int=False, message='The result is'):
    if operation == "add" and make_int == True:
        return print(f'{message} {int(a+b)}')
    elif operation == "add":
        return print(f'{message} {a+b}')
    elif operation == "subtract" and make_int == True:
        return print(f'{message} {int(a-b)}')
    elif operation == "subtract":
        return print(f'{message} {a-b}')
    elif operation == "multiply" and make_int == True:
        return print(f'{message} {int(a*b)}')
    elif operation == "multiply":
        return print(f'{message} {a*b}')
    elif operation == "divide" and make_int == True:
        return print(f'{message} {int(a/b)}')
    elif operation == "divide":
        return print(f'{message} {a/b}')
    else:
        return print("None")

    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """


calculate('add', 2.5, 4)
calculate('subtract', 4, 1.5, make_int=True)
calculate('multiply', 1.5, 2)
calculate('divide', 10, 4, message='I got')
calculate('foo', 2, 3)