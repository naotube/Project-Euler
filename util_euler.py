from math import sqrt

primes = [2,3]

def is_prime(number):
    """if num is a prime number, returns True, else returms False
    >>> is_prime(3)
    True
    >>> is_prime(23)
    True
    >>> is_prime(39)
    False
    >>> is_prime(437)
    False
    """
    if number < 2:
        return False

    while True:
        if primes[-1] > sqrt(number):
            break
        primes_next = next_prime(primes[-1])
        if primes_next not in primes:
            primes.append(primes_next)

    for i in primes:
        if i > sqrt(number):
            break
        if number % i == 0:
            return False
    return True

def prime_generator(maximum=1000000, minimum=2):
    primes = []
    count = 1
    UNIT_LENGTH = 1000
    queue = []
    for i in range(2,UNIT_LENGTH):
        queue.append(i)
    while queue[0] < maximum:
        if len(queue) < 10:
            following_numbers = []
            for i in range(UNIT_LENGTH):
                following_numbers.append(count * UNIT_LENGTH + i)
            count += 1
            following_queue = []
            for i in following_numbers:
                following_queue_numbers = True
                for j in primes:
                    if j > sqrt(maximum):
                        break
                    if i % j == 0:
                        following_queue_numbers = False
                        break
                if following_queue_numbers:
                    following_queue.append(i)
            queue = queue + following_queue

        primes.append(queue[0])
        if queue[0] >= minimum:
            yield queue[0]

        new_queue = []
        if queue[0] < sqrt(maximum):
            for i in queue:
                if not i % queue[0] == 0:
                    new_queue.append(i)
        else:
            new_queue = queue[1:]
        queue = new_queue

def next_prime(number):
    """returns a first prime number larger than num
    >>> next_prime(3)
    5
    >>> next_prime(13)
    17
    >>> next_prime(100)
    101
    """
    if number == 2:
        return 3
    if not is_prime(number):
        while True:
            number = number + 1
            if is_prime(number):
                return number
    while True:
        number = number + 2
        if is_prime(number):
            return number

def find_prime_factors(number):
    """
    returns list of prime factors of 'number'
    >>> find_prime_factors(24)
    [2, 2, 2, 3]
    >>> find_prime_factors(23)
    [23]
    """
    factors = []
    i = 2
    TARGET = number
    while i <= sqrt(TARGET):
        if number % i == 0:
            number = number / i
            factors.append(i)
        else:
            i = next_prime(i)
            if not i in primes:
                primes.append(i)
    if not number == 1:
        factors.append(int(number))
    return factors

def count_divisor(number):
    """
    counts how many divisors 'number' has
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
    """
    finds divisors of 'number'
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

def is_palindrome(string):
    """ if num is palindromic(:be read as same from both of right/left sides), return True

        >>> is_palindrome('123')
        False
        >>> is_palindrome('787')
        True
        >>> is_palindrome('9483')
        False
        >>> is_palindrome('5665')
        True
        >>> is_palindrome('56165')
        True
    """
    if string == string[::-1]:
        return True
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
