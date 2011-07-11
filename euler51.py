import util_euler

def replace_digit_in_number(number,index,replace):
    """
    >>> replace_digit_in_number(12345,[2],6)
    12645
    >>> replace_digit_in_number(13245768,[1,4,7],9)
    19249769
    """
    number = str(number)
    replace = str(replace)

    replaced = ""
    for i in range(len(number)):
        if i in index:
            replaced += replace
        else:
            replaced += number[i]
    return int(replaced)

def max_prime_family(number):
    """
    >>> max_prime_family(13)
    6
    >>> max_prime_family(56003)
    7
    """
    return 6

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    gen = util_euler.prime_generator()
    for i in gen:
        if max_prime_family(i) == 6:
            answer = i
            break
    print(i)
