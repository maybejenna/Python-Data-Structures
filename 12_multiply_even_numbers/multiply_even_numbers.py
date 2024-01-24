def multiply_even_numbers(nums):
    product_even_nums=1
    found_even = False
    for num in nums:
        if num % 2 == 0 :
            product_even_nums *= num
            found_even = True
    return product_even_nums if found_even \
    else  1
    # """Multiply the even numbers.
    #
    #     >>> multiply_even_numbers([2, 3, 4, 5, 6])
    #     48
    #
    #     >>> multiply_even_numbers([3, 4, 5])
    #     4
    #
    # If there are no even numbers, return 1.
    #
    #     >>> multiply_even_numbers([1, 3, 5])
    #     1
    # """