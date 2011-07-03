from math import sqrt

primes = [2,3]

def is_prime(num):
    """if num is a prime number, returns True, else returms False
    >>> is_prime(3)
    True
    >>> is_prime(23)
    True
    >>> is_prime(39)
    False
    """
    for i in primes:
        if i > sqrt(num):
            break
        if num % i == 0:
            return False
    return True

def next_prime(num):
    """returns a first prime number larger than num
    >>> next_prime(3)
    5
    >>> next_prime(13)
    17
    """
    if num == 2:
        return 3
    if not is_prime(num):
        while True:
            num = num + 1
            if is_prime(num):
                return num
    while True:
        num = num + 2
        if is_prime(num):
            return num

def find_prime_factors(num):
    """returns list of prime factors
    >>> find_prime_factors(24)
    [2, 2, 2, 3]
    >>> find_prime_factors(23)
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

def count_divisor(number):
    """returns how many divisors 'number' has
    >>> count_divisor(28)
    6
    >>> count_divisor(4)
    3
    >>> count_divisor(27)
    4
    """
    factors = find_prime_factors(number)
    checked = []
    divisors = 1
    for i in factors:
        if i not in checked:
            divisors = divisors * (factors.count(i) + 1)
            checked.append(i)
    return divisors

def find_divisors(number, proper=False):
    """finds divisors of a number
    >>> find_divisors(220)
    [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110, 220]
    >>> find_divisors(220,True)
    [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]
    >>> find_divisors(284)
    [1, 2, 4, 71, 142, 284]
    >>> find_divisors(284,True)
    [1, 2, 4, 71, 142]
    """
    divisors = [number]
    factors = find_prime_factors(number)
    if number < 2:
        if proper:
            return []
        else:
            if number == 1:
                return [1]
            else:
                return []
    while True:
        new_divisor_found = False
        for i in factors:
            for j in divisors:
                quotient = j/i
                if j % i == 0:
                    if quotient not in divisors:
                        divisors.append(int(quotient))
                        new_divisor_found = True
        if not new_divisor_found:
            break
    divisors.sort()
    if proper:
        divisors.remove(divisors[-1])
    return divisors

def is_abundant(number):
    """
    if sum of proper divisors of a number exceeds the number, return True.
    else, False.
    >>> is_abundant(12)
    True
    >>> is_abundant(13)
    False
    >>> is_abundant(28)
    False
    >>> is_abundant(0)
    False
    """
    divisors = find_divisors(number, True)
    if sum(divisors) > number:
        return True
    else:
        return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    LIMIT = 28123

    abundant_numbers = []
    for i in range(LIMIT + 1):
        if is_abundant(i):
            abundant_numbers.append(i)

    can_be_written_in_sum_of_two_abundant = []
    for i in range(LIMIT + 1):
        for j in abundant_numbers:
            if i - j < 0:
                break
            if i - j in abundant_numbers:
                can_be_written_in_sum_of_two_abundant.append(i)
                break
    print(sum([i for i in range(LIMIT + 1)])-sum(can_be_written_in_sum_of_two_abundant))

