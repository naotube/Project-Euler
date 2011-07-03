from math import sqrt

primes = [2,3]

def is_prime(num):
    """if num is a prime number, returns True, else returms False"""
    for i in primes:
        if i > sqrt(num):
            break
        if num % i == 0:
            return False
    return True

def next_prime(num):
    """returns a first prime number larger than num"""
    if num == 2:
        return 3
    while 1:
        num = num + 2
        if is_prime(num):
            return num

def prime_factors(num):
    """returns list of prime factors
    >>> prime_factors(24)
    [2, 2, 2, 3]
    >>> prime_factors(23)
    [23]
    """
    factors = []
    i = 2
    TARGET = num
    while i <= sqrt(TARGET):
        if num % i == 0:
            num = num / i
            factors.append(i)
        else:
            i = next_prime(i)
            if not i in primes:
                primes.append(i)
    if not num == 1:
        factors.append(int(num))
    return factors

def triangle(number):
    """returns 1+2+3+...+number
    >>> triangle(1)
    1
    >>> triangle(10)
    55
    """
    triangle = 0
    for i in range(1,number+1):
        triangle = triangle + i
    return triangle

def count_divisor(number):
    """returns how many divisors 'number' has
    >>> count_divisor(28)
    6
    >>> count_divisor(4)
    3
    >>> count_divisor(27)
    4
    """
    factors = prime_factors(number)
    checked = []
    divisors = 1
    for i in factors:
        if i not in checked:
            divisors = divisors * (factors.count(i) + 1)
            checked.append(i)
    return divisors

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    tri = 0
    for i in range(0,100000000):
        tri = tri + i
        if count_divisor(tri) > 500:
            print(tri)
            break

