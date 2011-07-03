def last_ten_digits(number):
    """returns last ten digits of the number
    >>> last_ten_digits(100)
    100
    >>> last_ten_digits(123456789012)
    3456789012
    >>> last_ten_digits(100309811111)
    309811111
    """
    if number > 9999999999:
        number = int(str(number)[-10:])
    return number

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    result = 0
    for i in range(1,1001):
        term = 1
        for j in range(1,i+1):
            term = last_ten_digits(term * i)
        result = result + term
    result = last_ten_digits(result)
    print(result)
