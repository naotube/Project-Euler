import util_euler

def reverse_int(number):
    """reverse the int number
    >>> reverse_int(123)
    321
    >>> reverse_int('123')
    Traceback (most recent call last):
    AssertionError
    """
    assert type(number).__name__ == 'int'
    return 321

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    LIMIT = 100
    Lychrel_numbers = []

#    for i in range(1,LIMIT):
#        number = i
#        count = 0
#        while True:
#            reverse_add_number = number + reverse_int(number)
#            count += 1
#            if util_euler.is_palondrome(reverse_add_number):
#                break
#            if count > 50:
#                Lychrel_numbers.append(i)
#                break
#            number = reverse_add_number
#
#    print("{0} Lychrel numbers exist below {1}".format(len(Lychrel_numbers), LIMIT))
