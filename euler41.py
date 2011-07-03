import util_euler

def is_pandigital(number):
    """if a number includes all the digits 1 to n exactly once, the number is pandigital
    >>> is_pandigital(1254)
    False
    >>> is_pandigital(233145)
    False
    >>> is_pandigital(1)
    True
    >>> is_pandigital(193728465)
    True
    """
    num_string = str(number)
    for d in range(len(num_string)):
        if not num_string.count(str(d+1)) == 1:
            return False
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    prime = util_euler.prime_generator(7654321)
    result = 0
    for i in prime:
        if is_pandigital(i):
            result = i
    print(result)
