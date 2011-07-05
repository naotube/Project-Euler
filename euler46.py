import util_euler
from math import sqrt

if __name__ == "__main__":
    number = 3
    while True:
        odd_divisors = util_euler.find_divisors(number, proper=True)
        odd_divisors.remove(1)
        for d in odd_divisors:
            if d % 2 == 0:
                odd_divisors.remove(d)
        if not all((number / d) % 2 == 0 for d in odd_divisors):
            if all(not util_euler.is_prime(number - (i ** 2) * 2) for i in range(int(sqrt(number)))):
                answer = number
                break
        number += 2
    print("answer: {0}".format(answer))
