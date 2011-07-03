import util_euler

def rotate(string):
    """
    e.g. in a case string '1234', return '2341'. for '2341', returns '3412', and like that.
    >>> rotate('1234')
    '2341'
    >>> rotate('23456')
    '34562'
    >>> rotate('101')
    '011'
    """
    return string[1:] + string[:1]

def is_circular_prime(number):
    """if number is a circular prime, return True, else False.
    >>> is_circular_prime(37)
    True
    >>> is_circular_prime(197)
    True
    >>> is_circular_prime(101)
    False
    >>> is_circular_prime(123)
    False
    """
    num_string = str(number)
    for i in range(len(num_string)):
        if not util_euler.is_prime(int(num_string)):
            return False
        num_string = rotate(num_string)
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    LIMIT = 1000000

    circular_primes = []

    prime = util_euler.prime_generator(LIMIT)
    primes = []
    for i in prime:
        primes.append(i)

    for i in primes:
        if i in circular_primes:
            continue
        num_string = str(i)
        if is_circular_prime(i):
            for j in range(len(num_string)):
                if int(num_string) not in circular_primes:
                    circular_primes.append(int(num_string))
                num_string = rotate(num_string)

    print(circular_primes)
    print(len(circular_primes))
